with open("pets.txt", "r") as file:
    sum = 0
    for line in file:
        line = line.split(" ")
        sum+=len(line)

print(sum)
