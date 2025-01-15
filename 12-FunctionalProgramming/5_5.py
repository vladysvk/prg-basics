arr = [i for i in range(21)]
arr = list(filter(lambda x: x%2 == 0 and x%3==0, arr))
print(arr)