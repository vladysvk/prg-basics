import csv

with open("integers.txt", "w", newline="") as file:
    writer = csv.writer(file)

    for i in range(1, 101):
        writer.writerow([i, i**2, i**3])