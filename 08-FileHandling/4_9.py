import csv

with open("it_company.csv") as file:
    csv_content = csv.DictReader(file)
    for dictionary in csv_content:
        if dictionary["Job Title"] == "Graphic Designer":
            print(f"{dictionary['First Name']} {dictionary['Last Name']},{dictionary['Email']}")

