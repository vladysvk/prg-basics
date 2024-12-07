arr = [[-38, 19], [5,40],[-7,11],[29,16]]
new_arr = []
for i in arr:
    for j in i:
        new_arr.append(j)

new_arr = sorted(new_arr)
smallest = new_arr[0]
largest = new_arr[-1]
row_smallest = 0
collumn_smallest = 0
row_largest = 0
collumn_largest = 0


for item in range(len(arr)):
    for num in arr[item]:
        if num == smallest:
            row_smallest = item+1
            collumn_smallest = arr[item].index(num) + 1
        elif num == largest:
            row_largest = item+1
            collumn_largest = arr[item].index(num) + 1

print(row_smallest,collumn_smallest,"\n",row_largest,collumn_largest)
