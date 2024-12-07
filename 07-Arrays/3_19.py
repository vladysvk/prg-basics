arr = [1,5,12,62,6,322,161,1447,1,17,1,8,1,5,9,2,1]
num = int(input("Enter the number: "))
elements = 0
for i in arr:
    if i > num:
        elements+=1

print(elements)