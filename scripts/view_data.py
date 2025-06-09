from pymongo import MongoClient
import pandas as pd

# Σύνδεση στη βάση
client = MongoClient("mongodb://localhost:27017/")
db = client["smartcart_db"]

# Λίστα με όλα τα collections
collections = ["products", "categories", "users", "carts", "cart_items"]

def show_collection(name):
    print(f"\nΣυλλογή: {name}")
    cursor = db[name].find({}, {"_id": 0})  # Δεν εμφανίζω το _id για καθαρότητα
    df = pd.DataFrame(cursor)

    if df.empty:
        print("Δεν υπάρχουν εγγραφές.")
    else:
        print(df.head(20))  # Εμφανίζω τις 10 πρώτες εγγραφές

    return df

# Εμφανίζω κάθε πίνακα
dataframes = {}
for col in collections:
    df = show_collection(col)
    dataframes[col] = df  # Αν θες να έχεις πρόσβαση αργότερα