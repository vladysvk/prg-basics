import random
arr = [[random.randint(1, 100) for i in range(5)] for i in range(3)]
for item in arr:
    for num in item:
        print(num, end=" ")
    print()
print()

for i in range(len(arr)):
    arr[i][0], arr[i][-1] = arr[i][-1], arr[i][0]

for item in arr:
    for num in item:
        print(num, end=" ")
    print()