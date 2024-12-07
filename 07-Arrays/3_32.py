import random
arr = [[random.randint(1, 100) for i in range(5)] for i in range(3)]
for item in arr:
    for num in item:
        print(num, end=" ")
    print()
print()

arr[0], arr[-1] = arr[-1], arr[0]

for item in arr:
    for num in item:
        print(num, end=" ")
    print()