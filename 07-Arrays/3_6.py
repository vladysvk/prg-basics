arr = [15, 8, 31, 47, 2, 19]
n = 0
sum = 0 

while n < len(arr):
    print(arr[n], end=" ")
    sum += arr[n]
    n += 1

print()
print(f"{sum/len(arr): .2f}")

