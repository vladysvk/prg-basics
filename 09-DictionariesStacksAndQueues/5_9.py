import csv

count = {}

with open("province.csv", encoding="utf-8") as file:
    provinces = list(csv.DictReader(file))
    with open("vehicle.txt") as second_file:
        for line in second_file:
            line = line.strip()
            for province in provinces:
                if line[0] == province["Letter"]:
                    if province["Name"] in count:
                        count[province["Name"]] += 1
                    else:
                        count[province["Name"]] = 1     

for province in count:
    print(f"{province}: {count[province]}")