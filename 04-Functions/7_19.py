def main():
    print(f(513553007))

def f(number):
    numbers_count = {}
    sum = 0
    for i in str(number):
        if i in numbers_count:
            numbers_count[i] += 1
        else:
            numbers_count[i] = 1 

    for i in numbers_count:
        if numbers_count[i] > 1:
            sum += int(i) * numbers_count[i] 
    return sum

if __name__ == "__main__":
    main()