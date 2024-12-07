def number_of_words(text):
    text = text.split(" ")
    return len(text)

def ordered_by_len(text):
    text = text.split(" ")
    n = len(text) - 1
    sorted = True

    while sorted:
        sorted = False

        for i in range(n):
            if len(text[i]) < len(text[i+1]):
                text[i], text[i+1] = text[i+1], text[i]
                sorted = True
    return text

def oredered_alphabetically(text):
    text = text.split(" ")
    return sorted(text)


