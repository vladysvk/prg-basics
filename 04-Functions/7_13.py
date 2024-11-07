def main():
    print(f(4))

def f(n):
    range_of_numbers = ""
    for i in range(1, n + 1):
        range_of_numbers+=str(i)
    return range_of_numbers

if __name__ == "__main__":
    main()