import random
from datetime import datetime, timedelta
from bson import ObjectId
from app.utils.constructors import create_cart, create_cart_item
from app.db.DB_config import users_collection, products_collection, carts_collection, cart_items_collection

# Ανάκτηση όλων των χρηστών και των προϊόντων από τη βάση
users = list(users_collection.find({}))
products = list(products_collection.find({}))

# Ορισμός ημερομηνίας εκκίνησης για τα καλάθια (π.χ. από 1 Ιανουαρίου)
start_date = datetime(datetime.now().year, 1, 1)

# Για κάθε χρήστη δημιουργώ καλάθια
for user in users:
    user_id = user["_id"]
    email = user["email"]

    # Αν είναι ο demo χρήστης => 25 καλάθια, αλλιώς 15
    num_carts = 25 if "demo" in email else 15

    for i in range(num_carts):
        # Υπολογισμός τυχαίας ημερομηνίας δημιουργίας
        days_offset = (i * 6) + random.randint(-2, 2)
        created_at = start_date + timedelta(days=days_offset)

        # Δημιουργία καλαθιού
        cart = create_cart(user_id=user_id, status="ordered", created_at=created_at)
        result = carts_collection.insert_one(cart)
        cart_id = result.inserted_id

        # Επιλογή 7–14 τυχαίων προϊόντων για το καλάθι
        selected_products = random.sample(products, random.randint(7, 14))

        for product in selected_products:
            quantity = random.randint(1, 3)
            cart_item = create_cart_item(
                cart_id=cart_id,
                product_id=product["_id"],
                quantity=quantity,
                created_at=created_at
            )
            cart_items_collection.insert_one(cart_item)

print("Ολοκληρώθηκε η δημιουργία εικονικών αγορών.")
