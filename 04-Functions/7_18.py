def main():
    print(f("integrated development environment"))

def f(sentence):
    new_sentence = ""
    for letter in sentence:
        if letter == " ":
            pass
        else:
            new_sentence+=letter
    return new_sentence.strip()
if __name__ == "__main__":
    main()