import module74

def main():
    text = "You never get a second chance to make a first impression"
    letter = input("Enter the letter: ")

    number = module74.find_letter(text, letter)
    print(f"The number of letter '{letter}': {number}")


if __name__ == "__main__":
    main()