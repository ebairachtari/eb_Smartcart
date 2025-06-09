import pandas as pd
from app.scrapers.efresh_scraper import scrape_efresh
from app.scrapers.marketin_scraper import scrape_marketin
from datetime import datetime
import os

# Διαβάζω το αρχείο CSV που έχω φτιάξει με τα URLs των προϊόντων
df_urls = pd.read_csv("seed_data/products_url.csv")

# Φτιάχνω μια λίστα όπου θα αποθηκεύσω τα αποτελέσματα του scraping
scraped_data = []

# Για κάθε γραμμή του πίνακα (κάθε προϊόν), κάνω scraping από τα δύο e-shops
for index, row in df_urls.iterrows():
    
    print(f"\nΞεκινάω scraping για προϊόν: {row['name']}")
    
    # Παίρνω τα URLs για efresh και marketin
    efresh_url = row['efresh_url']
    marketin_url = row['marketin_url']
    
    # Εκτελώ scraping για κάθε κατάστημα
    data_efresh = scrape_efresh(efresh_url)
    data_marketin = scrape_marketin(marketin_url)

    sources_efresh = data_efresh.get("scraped_from") if data_efresh else []
    sources_marketin = data_marketin.get("scraped_from") if data_marketin else []

    # Ενώνω τα δεδομένα σε ένα dictionary
    combined_data = {
        "product_name": row['name'],
        "category": row['category'],
        "efresh_url": efresh_url,
        "marketin_url": marketin_url,
        # Αν υπάρχει αποτέλεσμα, παίρνω τα στοιχεία, αλλιώς βάζω κενό
        "price_efresh": data_efresh.get("price_efresh") if data_efresh else "",
        "price_per_unit_efresh": data_efresh.get("price_per_unit") if data_efresh else "",
        "description_efresh": data_efresh.get("description") if data_efresh else "",
        "image_url_efresh": data_efresh.get("image_url") if data_efresh else "",
        "price_marketin": data_marketin.get("price_marketin") if data_marketin else "",
        "price_per_unit_marketin": data_marketin.get("price_per_unit_marketin") if data_marketin else "",
        "nutritional_info_marketin": data_marketin.get("nutritional_info") if data_marketin else "",
        "scraped_from": sources_efresh + sources_marketin,
        "efresh_url": efresh_url,
        "marketin_url": marketin_url
    }
    
    # Το προσθέτω στη λίστα με τα δεδομένα
    scraped_data.append(combined_data)

# Φτιάχνω DataFrame με όλα τα δεδομένα που συνέλεξα
df_scraped = pd.DataFrame(scraped_data)

# Χρησιμοποιώ τον φάκελο που έχω φτιάξει για να αποθηκεύω ιστορικό
output_folder = "scraped_outputs"

# Φτιάχνω όνομα αρχείου με βάση ημερομηνία-ώρα μέσα στον φάκελο
filename = os.path.join(output_folder, f"scraped_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv")

# Αποθηκεύω τα δεδομένα
df_scraped.to_csv(filename, index=False, encoding="utf-8-sig")

print(f"\nΟλοκληρώθηκε το scraping και η αποθήκευση στο αρχείο: {filename}")