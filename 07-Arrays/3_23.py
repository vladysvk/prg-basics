import MyText

def main():
    text = "An apple a day keeps the doctor away"
    print(MyText.number_of_words(text))
    print(MyText.ordered_by_len(text))
    print(MyText.oredered_alphabetically(text))
    


if __name__ == "__main__":
    main()