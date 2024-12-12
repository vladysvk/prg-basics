import csv

with open("books_fantasy.csv", "w", newline="") as fantasy:
    fieldnames = ["Title", "Author", "Year"]
    csv.DictWriter(fantasy, fieldnames=fieldnames).writeheader()
with open("books_historical.csv", "w", newline="") as historical:
    fieldnames = ["Title", "Author", "Year"]
    csv.DictWriter(historical, fieldnames=fieldnames).writeheader()
with open("books_romance.csv", "w", newline="") as romance:
    fieldnames = ["Title", "Author", "Year"]
    csv.DictWriter(romance, fieldnames=fieldnames).writeheader()
with open("books_classic.csv", "w", newline="") as classic:
    fieldnames = ["Title", "Author", "Year"]
    csv.DictWriter(classic, fieldnames=fieldnames).writeheader()

with open("books.csv") as file:
    reader = csv.DictReader(file)
    for dictionary in reader:
        if dictionary["Genre"] == "Fantasy":
            with open("books_fantasy.csv", "a", newline="") as fantasy:
                csv.DictWriter(fantasy, fieldnames=fieldnames).writerow({"Title": dictionary["Title"], "Author": dictionary["Author"], "Year": dictionary["Year"]})
        elif dictionary["Genre"] == "Historical":
            with open("books_historical.csv", "a", newline="") as historical:
                csv.DictWriter(historical, fieldnames=fieldnames).writerow({"Title": dictionary["Title"], "Author": dictionary["Author"], "Year": dictionary["Year"]})
        elif dictionary["Genre"] == "Romance":
            with open("books_romance.csv", "a", newline="") as romance:
                csv.DictWriter(romance, fieldnames=fieldnames).writerow({"Title": dictionary["Title"], "Author": dictionary["Author"], "Year": dictionary["Year"]})
        elif dictionary["Genre"] == "Classic":
            with open("books_classic.csv", "a", newline="") as classic:
                csv.DictWriter(classic, fieldnames=fieldnames).writerow({"Title": dictionary["Title"], "Author": dictionary["Author"], "Year": dictionary["Year"]})
