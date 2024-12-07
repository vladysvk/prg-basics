arr = [15, 8, 31, 47, 2, 19]

print("old array", arr)
print("new array", [arr[i] for i in range(len(arr)-1, -1, -1)])

