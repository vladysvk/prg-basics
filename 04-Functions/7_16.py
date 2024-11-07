def main():
    print(f(5))

def f(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return f(n - 1) + f(n - 2)
    

if __name__ == "__main__":
    main()