numbers = (50,20,40,50,30,50)
value = 50
occurences = 0

for i in numbers:
    if i == value:
        occurences += 1
print(occurences)