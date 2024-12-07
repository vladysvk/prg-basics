arr = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]

longest = len(arr[0])
longest_name = arr[0]
for name in arr:
    if len(name) > longest:
        longest = len(name)
        longest_name = name
        
print(longest_name)