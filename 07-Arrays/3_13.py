def main():
    n  = int(input("Enter the number: "))
    arr = [15, 38, 7, 23, 14]
    if occurs(n, arr):
        print(f"number {n} appears in the array")
    else:
        print(f"number {n} does not appear in the array")

def occurs(n, arr):
    if n in arr:
        return True
    return False


if __name__ == "__main__":
    main()