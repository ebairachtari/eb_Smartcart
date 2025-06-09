# SmartCart

## Περιγραφή
Ένα ολοκληρωμένο Python e‑commerce σύστημα με Flask, MongoDB, Streamlit και AI τεχνολογίες.

---

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

## Βάση Δεδομένων & Αρχικοποίηση Δεδομένων

Η εφαρμογή χρησιμοποιεί **MongoDB (τοπικά)** ως σύστημα αποθήκευσης δεδομένων. Δεν απαιτούνται cloud υπηρεσίες.

### Κύριες Συλλογές (collections):
- `products`: προϊόντα που έχουν εξαχθεί μέσω scraping από e-Fresh & MarketIN (τιμή, περιγραφή, εικόνα, διαθεσιμότητα)
- `categories`: προκαθορισμένες κατηγορίες προϊόντων
- `users`: στοιχεία χρηστών με hashed κωδικούς
- `carts`: καλάθια χρηστών με κατάσταση (status), συνολικό κόστος κ.ά.
- `cart_items`: προϊόντα μέσα σε κάθε καλάθι, με ποσότητες και τιμές

## Scripts για Εισαγωγή & Εμπλουτισμό Δεδομένων

### Μαζικό Scraping
```bash
python scripts/run_scraper.py
```

### Κατηγορίες
```bash
python scripts/insert_categories_to_mongo.py
```

### Προϊόντα
```bash
python scripts/insert_products_to_mongo.py
```

### Bulk Carts
```bash
python scripts/simulate_bulk_carts.py
```

## Εκτέλεση Backend & Postman Collection

```bash
python main.py       
```

> Στο φάκελο `Postman_Collection/` υπάρχουν όλα τα endpoints και το ρυθμισμένο environment για τα tokens έτοιμα για εισαγωγή στον Postma

## Frontend

```bash
streamlit run ui/Σύνδεση.py  
```

## Δομή Φακέλων

```
app/             # Core logic & routes
scripts/         # Scripts για seed & scraping
seed_data/       # Αποτελέσματα από τα scripts για seed
ui/              # Το Streamlit interface
tests/           # Δοκιμές scraping
scraped_outputs/ # Αποθηκευμένα scraping αποτελέσματα
```

>*Αναπτύχθηκε αποκλειστικά για εκπαιδευτικούς σκοπούς.*
