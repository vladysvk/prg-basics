def main():
    for num in arr:
        print(f"{num}: {star(num)}")


arr = [2, 6, 4, 9, 7]

def star(n):
    string = ""
    for i in range(n):
        string += "*"
    return string

if __name__ == "__main__":
    main()