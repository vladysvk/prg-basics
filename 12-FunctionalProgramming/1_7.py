def main():
    number = int(input("Enter a number: "))
    is_even = lambda number: number % 2 == 0
    print(f"Number is even: {is_even(number)}")


if __name__ == "__main__":
    main()