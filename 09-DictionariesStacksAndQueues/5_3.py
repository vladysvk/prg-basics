def main():
    word = input("Enter a word to translate: ")
    print(translator(word))

def translator(word):
    translations = {'computer': 'komputer','mouse': 'myszka','keyboard': 'klawiatura','printer': 'drukarka'}
    if word in translations:
        return translations[word]
    else:
        return "Can't translate the word"

if __name__ == "__main__":
    main()