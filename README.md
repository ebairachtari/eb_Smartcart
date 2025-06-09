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
project_root/
├── app/
│   ├── routes/              # Flask API endpoints για authentication, carts, products, analytics, AI
│   ├── services/            # Business λογική (MongoDB queries, έλεγχοι, επεξεργασία δεδομένων)
│   ├── db/                  # Ρύθμιση σύνδεσης MongoDB και CRUD functions (DB_config, DB_repository)
│   ├── model/               # Pydantic models για validation (User, CartItem)
│   ├── scrapers/            # Συναρτήσεις scraping (e-Fresh, MarketIN)
│   ├── utils/               # Βοηθητικά αρχεία: constructors για documents, constants
│   └── middleware/          # Έλεγχος JWT με custom @token_required decorator
│
├── ui/                      # Streamlit interface (πολλαπλές σελίδες, login, προβολή προϊόντων, στατιστικά)
│
├── scripts/                 # Scripts για scraping, εισαγωγή προϊόντων/κατηγοριών, ενημέρωση αποθέματος, δημιουργία bulk carts
│
├── seed_data/               # Αρχεία CSV με αρχικά URLs, κατηγορίες και stock
│
├── scraped_outputs/         # Καταγεγραμμένα αποτελέσματα scraping (.csv με timestamp)
│
├── Postman_Collection/      # Postman collection & environment για δοκιμή όλων των endpoints
│
├── requirements.txt         # Όλες οι απαιτούμενες Python βιβλιοθήκες
├── .env                     # Περιβαλλοντικές μεταβλητές (MONGO_URI, JWT_SECRET_KEY) [εκτός Git]
├── README.md                # Τεχνική τεκμηρίωση έργου
└── main.py                  # Κύρια είσοδος εφαρμογής Flask
```

>*Αναπτύχθηκε αποκλειστικά για εκπαιδευτικούς σκοπούς.*
