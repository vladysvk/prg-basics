import months

def main():
    number = int(input("Enter month: "))
    month = months.get_month(number)
    print(f"The name of month {number} is {month}")



if __name__ == "__main__":
    main()