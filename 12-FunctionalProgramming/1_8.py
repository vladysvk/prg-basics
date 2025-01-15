def main():
    name = input("Enter your name: ")
    surname = input("Enter your surname: ")
    func = lambda name, surname: f"{name[0]}{surname[0]}"
    print(func(name,surname))

if __name__ == "__main__":
    main()