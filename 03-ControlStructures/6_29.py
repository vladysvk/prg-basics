N = int(input("Enter "))


for i in range(2, N+1):
    prime = True
    if i == 2:
        print(i)
        continue
    for j in range(2, i):
        if i % j == 0:
            prime = False
            break
    if prime:
        print(i)