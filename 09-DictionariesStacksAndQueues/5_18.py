import json

with open("dogs.json") as file:
    data = json.load(file)

for cell in data:
    for key, value in cell.items():
        if cell["age"] < 4:
            print(key , ":", value)
    print()

