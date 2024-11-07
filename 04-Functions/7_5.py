import module75

def main():
    number = int(input("Enter the number: "))
    x = int(input("Enter start of the range: "))
    y = int(input("Enter end of the range: "))

    is_within_range = module75.within_range(x, y, number)

    if is_within_range:
        print(f"Number {number} in the range <{x},{y}>: yes")
    else:
        print(f"Number {number} in the range <{x},{y}>: no")

if __name__ == "__main__":
    main()