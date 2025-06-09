import csv
from app.db.DB_config import products_collection

# Διαβάζω το CSV
with open("seed_data/products_stock.csv", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)

    updated = 0
    not_found = []

    for row in reader:
        name = row["name"].strip()
        stock = int(row["stock"])

        result = products_collection.update_one(
            {"name": name},
            {"$set": {"stock": stock}}
        )

        if result.modified_count > 0:
            print(f"Ενημερώθηκε stock για: {name} → {stock}")
            updated += 1
        else:
            not_found.append(name)

print(f"Συνολικά ενημερώθηκαν {updated} προϊόντα.")
if not_found:
    print("Δεν βρέθηκαν στη βάση τα παρακάτω προϊόντα:")
    for name in not_found:
        print(" -", name)