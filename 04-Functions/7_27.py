def main():
    print(f("1082"))
    print(f("2035"))
    print(f("1114"))
    print(f("7071"))


def f(product_code):
    if len(product_code) != 4 and  not product_code.isdigit():
        return False
    
    sum = int(product_code[0]) + int(product_code[1]) + int(product_code[2])
    control_digit = int(product_code[3])

    remainder  = sum % 7
    
    return remainder == control_digit

if __name__ == "__main__":
    main()