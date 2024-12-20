import json
product = {}

# read product data from keyboard
name = input("Enter the name of the product: ")
price = float(input("Enter the price Ex.(20.99): "))
paid = bool(input("Paid true or false: "))
# save product data to json file

product["name"] = name
product["price"] = price
product["paid"] = paid

with open("product.json", "w") as file:
    json.dump(product, file, indent=1)