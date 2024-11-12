def main():
    print(f("University"))
    print(f("UE"))
    print(f("x"))
    print(f(""))

def f(text):
    text = text.strip()
    if len(text) <= 1:
        return text
    new_text = text[0]
    for i in range(1, len(text)):
        new_text += f"-{text[i]}"
    return new_text

if __name__ == "__main__":
    main()