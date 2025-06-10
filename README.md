# SmartCart

## Περιγραφή
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
Αν κατά την εκτέλεση κάποιου script εμφανιστεί σφάλμα τύπου `ModuleNotFoundError: No module named 'app'`, παρακαλώ τρέξτε την εντολή ως εξής:

```bash
$env:PYTHONPATH = "."; python scripts/run_scraper.py


## Εκτέλεση Backend & Postman Collection

```bash
python main.py       
```

> Στο φάκελο `Postman_Collection/` υπάρχουν όλα τα endpoints και το ρυθμισμένο environment για τα tokens έτοιμα για εισαγωγή στον Postman.
> Τα endpoints προστατεύονται με JWT authentication. Το token αποθηκεύεται στο Postman environment και χρησιμοποιείται αυτόματα σε κάθε προστατευμένο request.


## Εκτέλεση Frontend

```bash
streamlit run ui/Σύνδεση.py  
```

## Δομή Φακέλων

```bash
eb_Smartcart/

├── app/                       # Κύρια λογική της εφαρμογής (Flask backend)
│   ├── db/                    # Σύνδεση και λειτουργίες με MongoDB
│   │
│   ├── middleware/            # Custom JWT decorator για προστασία endpoints
│   │
│   ├── model/                 # Pydantic μοντέλα για validation
│   │
│   ├── routes/                # Όλα τα API endpoints
│   │
│   ├── scrapers/              # Συναρτήσεις scraping για τα e-shops
│   │
│   ├── services/              # Business λογική & queries (Mongo, AI, ML)
│   │
│   └── utils/                 # Χρήσιμες συναρτήσεις, constructors, σταθερές
│
├── scraped_outputs/           # Αποτελέσματα scraping (.csv)
│
├── scripts/                   # Scripts αρχικοποίησης & επεξεργασίας
│
├── seed_data/                 # CSV αρχεία με URLs, stock, κατηγορίες
│
├── ui/                        # UI (Streamlit Frontend)
│   ├── Σύνδεση.py             # Εκκίνηση UI
│
├── main.py                    # Εκκίνηση Flask backend
```

>*Αναπτύχθηκε αποκλειστικά για εκπαιδευτικούς σκοπούς.*
