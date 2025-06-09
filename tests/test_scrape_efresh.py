from app.scrapers.efresh_scraper import scrape_efresh

test_url = "https://www.e-fresh.gr/el/ariani-15-lipara-mebgal-500-ml"
result = scrape_efresh(test_url)

if result:
    print("Δεδομένα προϊόντος από e-Fresh:")
    for k, v in result.items():
        print(f"{k}: {v}")
else:
    print("Το scraping δεν πέτυχε.")