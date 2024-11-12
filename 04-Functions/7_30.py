def main():
    print(sum_natural(3))

def sum_natural(n):
    if n == 1:
        return 1
    else:
        return n + sum_natural(n - 1) 
if __name__ == "__main__":
    main()