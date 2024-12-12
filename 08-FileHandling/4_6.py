lines = 0
characters = 0
words = 0
with open("books.csv") as file:
    for line in file:
        lines+=1
with open("books.csv") as file:
    books = file.read()

for line in books:
    characters+=1

with open("books.csv") as file:
    for line in file:
        line = line.split(",")
        words+=len(line)
print(lines)
print(characters)
print(words)