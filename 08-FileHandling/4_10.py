import csv


with open("clothing.csv") as file:
    data = csv.DictReader(file)
    for dictionary in data:
        if float(dictionary["Price"]) < 60 and float(dictionary["Stock_Quantity"]) < 40:
            print(dictionary["Product_Name"])
