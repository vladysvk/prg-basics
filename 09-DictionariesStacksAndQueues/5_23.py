import json

with open("euro.json") as file:
    data = json.load(file)["rates"]

print(f"Date                    No               Mid\n==============================================")
for cell in data:
    for value in cell.values():
        print(value, end="      ")
    print()