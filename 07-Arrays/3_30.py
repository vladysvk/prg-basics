arr = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
for i in range(1, len(arr)+1):
    for j in range(1, len(arr[i-1])+1):
        arr[i-1][j-1] = j*i

for i in arr:
    for j in i:
        print(j, end=" ")
    print()            
