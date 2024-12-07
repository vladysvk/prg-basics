zeros = [
   [0,0,0],
   [0,0,0],
   [0,0,0]
]

for i in range(len(zeros)):
    for j in range(len(zeros[i])):
        if i == j:
            zeros[i][j] = 1


for i in range(len(zeros)):
    for j in range(len(zeros[i])):
        print(f"{zeros[i][j]}", end=" ")
    print(end="\n")