arr = [-15, 8, -31, 47, -2, 19]

max = arr[0]

for i in range(1, len(arr)):
    if arr[i] > max:
        max = arr[i]

print(max)

min = arr[0]

for i in range(1, len(arr)):
    if arr[i] < min:
        min = arr[i]

print(min)