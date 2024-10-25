decimal_number = int(input("Enter decimal number: "))
binary_number = ""

if decimal_number == 0:
    binary_number = "0000"
else:
    while decimal_number > 0:
        binary_number = str(decimal_number % 2) + binary_number
        decimal_number = decimal_number // 2 

print(f"{decimal_number}(10) = {binary_number}(2)")