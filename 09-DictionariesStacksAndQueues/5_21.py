import json
book = {
    "name": "Alghorithms and Data Structures",
    "year": 2007,
    "author": "unknown",
    "is_sold": True,
    "price": 20.99
}

with open("favourites.json", "w") as file:
    json.dump(book, file, indent=1)
