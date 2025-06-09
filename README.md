````markdown
# SmartCart 🛒

Ένα ολοκληρωμένο Python e‑commerce σύστημα με Flask, MongoDB, Streamlit και AI τεχνολογίες.

## Τεχνολογίες
- Backend: Flask + Flask‑JWT‑Extended
- DB: MongoDB (PyMongo)
- UI: Streamlit
- Web Scraping: Selenium + BeautifulSoup4
- ML: scikit‑learn (LogisticRegression, KMeans)
- AI: OpenAI GPT API
- Scripts για βάση: seed_data/* & scripts/*.py
- Postman collection για όλο το API

## Οδηγίες Setup

```bash
git clone https://github.com/ebairachtari/eb_Smartcart.git
cd eb_Smartcart

python -m venv venv
source venv/bin/activate  # ή venv\Scripts\activate

pip install -r requirements.txt
````

## Ρύθμιση Περιβάλλοντος

**Δημιουργία `.env`:**

```env
MONGO_URI=mongodb://localhost:27017
JWT_SECRET_KEY=super-secret-key
```

## Δημιουργία και "σπόρος" βάσης

```bash
python scripts/insert_categories_to_mongo.py
python scripts/insert_products_to_mongo.py
python scripts/simulate_bulk_carts.py
```

## Εκτέλεση Backend & Frontend

```bash
python main.py         # Εκκίνηση Flask backend στο http://127.0.0.1:5000
streamlit run ui/Main.py  # τη γραμμή UI
```

## Postman Collection

Βρίσκεται στο φάκελο `postman/` → εισαγωγή στον Postman → περιέχει όλα τα endpoints

## Δομή Φακέλων

```
app/             # Core logic & routes
scripts/         # scripts για seed & scraping
seed_data/       # αν θέλεις να κρατήσεις export JSON
ui/              # Το Streamlit interface
tests/           # Υποθέτω ότι περιέχει δοκιμές
scraped_outputs/ # Αποθηκευμένα scraping αποτελέσματα
```
