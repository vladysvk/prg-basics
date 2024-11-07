def hide(card_number):
    hidden_number = ""
    for num in range(len(card_number)):
        if 2 <= num <= 11:
            hidden_number += "*"
        else:
            hidden_number += card_number[num]
    return hidden_number