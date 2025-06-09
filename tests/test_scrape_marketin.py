from app.scrapers.marketin_scraper import scrape_marketin

# Παράδειγμα URL προϊόντος από το Market IN
test_url = "https://www.market-in.gr/el-gr/galaktokomika-proionta-psygeiou-galata-gala-fresko-ksinogala/mevgal-ariani-gala-agelados-xoris-gloutenh-1-5-500ml"

# Εκτελώ το scraping
result = scrape_marketin(test_url)

# Αν βρεθούν δεδομένα, τα εμφανίζω
if result:
    print("Δεδομένα προϊόντος από Market IN:")
    for k, v in result.items():
        print(f"{k}: {v}")
else:
    print("Το scraping δεν πέτυχε.")
