def main():
    print(factorial(5))

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == "__main__":
    main()