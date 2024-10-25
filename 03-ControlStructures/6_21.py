number = int(input("Enter the amount in PLN: "))
coins_5 = 0
coins_2 = 0
coins_1 = 0

while number > 0:
    if number >= 5:
        number -= 5
        coins_5 += 1
    elif number >= 2:
        number -= 2
        coins_2 += 1
    elif number >= 1:
        number -= 1
        coins_1 += 1
    else:
        print("Amount is negative")
print(f"5 PLN coins: {coins_5}")
print(f"2 PLN coins: {coins_2}")
print(f"1 PLN coins: {coins_1}")

