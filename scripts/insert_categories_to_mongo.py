import csv
from app.utils.constructors import create_category
from app.db.DB_config import categories_collection

# Διαβάζω το CSV αρχείο
with open("seed_data/categories_seed.csv", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        name = row["name"]

        # Ελέγχω αν υπάρχει ήδη η κατηγορία
        if not categories_collection.find_one({"name": name}):
            category_doc = create_category(name)
            categories_collection.insert_one(category_doc)
            print(f"Προστέθηκε κατηγορία: {name}")
        else:
            print(f"Υπάρχει ήδη: {name}")
