import pandas as pd
from app.utils.constructors import create_product
import os
import glob
from datetime import datetime
from app.db.DB_config import products_collection, categories_collection

# Εύρεση του πιο πρόσφατου CSV στον φάκελο scraped_outputs
folder = "scraped_outputs"
csv_files = glob.glob(os.path.join(folder, "*.csv"))
latest_file = max(csv_files, key=os.path.getctime)

print(f"Φορτώνω το πιο πρόσφατο αρχείο: {latest_file}")
df = pd.read_csv(latest_file, encoding="utf-8-sig")

# Εισαγωγή προϊόντων ένα προς ένα
for _, row in df.iterrows():
    product_name = row["product_name"]
    category_name = row.get("category") 

    # Βρίσκω το _id της κατηγορίας
    category_id = None
    if pd.notna(category_name):
        category_doc = categories_collection.find_one({"name": category_name})
        if category_doc:
            category_id = category_doc["_id"]
        else:
            print(f"Η κατηγορία δεν βρέθηκε στη βάση: {category_name}")

    # Υπολογισμός τελικής τιμής
    # Τιμές από scraping
    price_efresh = row.get("price_efresh")
    price_marketin = row.get("price_marketin")

    # Έκπτωση σε ποσοστό 5%
    discount_percent = 5
    discount_factor = 1 - (discount_percent / 100)

    # Υπολογισμός τελικής τιμής με έκπτωση
    final_price = None
    if pd.notna(price_efresh) and pd.notna(price_marketin):
        min_price = min(price_efresh, price_marketin)
        final_price = round(min_price * discount_factor, 2)
    elif pd.notna(price_efresh):
        final_price = round(price_efresh * discount_factor, 2)
    elif pd.notna(price_marketin):
        final_price = round(price_marketin * discount_factor, 2)

    scraped_from = row["scraped_from"]
    scraped_from_list = scraped_from.strip("[]").replace("'", "").split(", ") if pd.notna(scraped_from) else []

    efresh_url = row.get("efresh_url")
    marketin_url = row.get("marketin_url")

    # Δημιουργία προϊόντος
    product = create_product(
    name=product_name,
    price_efresh=price_efresh,
    price_per_unit_efresh=row.get("price_per_unit_efresh"),
    price_marketin=price_marketin,
    price_per_unit_marketin=row.get("price_per_unit_marketin"),
    final_price=final_price,
    category_id=category_id,
    description=row.get("description_efresh"),
    image_url=row.get("image_url_efresh"),
    nutrition=row.get("nutritional_info_marketin"),
    scraped_from=scraped_from_list,
    efresh_url=efresh_url,
    marketin_url=marketin_url,
    created_at=datetime.now()
    )
    
    # Ελέγχω αν το προϊόν υπάρχει ήδη στη βάση
    existing_product = products_collection.find_one({"name": product_name})
    if existing_product:
        print(f"Το προϊόν {product_name} υπάρχει ήδη στη βάση.")
        continue

    # Εισαγωγή στη βάση
    products_collection.insert_one(product)

print("Ολοκληρώθηκε η εισαγωγή των προϊόντων στο MongoDB.")
