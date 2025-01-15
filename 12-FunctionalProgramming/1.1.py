

n1 = int(input("Enter the number: "))
n2 = int(input("Enter the number: "))

result = lambda x, y: (x+y)/2
print(f'The arithmetic mean of the numbers {n1} and {n2} is {result(n1, n2)}')