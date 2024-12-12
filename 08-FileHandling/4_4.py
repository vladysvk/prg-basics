with open("it_company.csv") as file:
    n = 0
    for line in file:
        print(line,end="")
        n+=1
        if n == 5:
            input("Press Enter key:")
            n = 0
            