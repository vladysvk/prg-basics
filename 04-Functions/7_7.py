def main(): 
    is_binary = f("10101001100")
    print(is_binary)
    



def f(binary_number):
    is_binary = True
    for integer in binary_number:
        if integer != "0" and integer != "1":
            return False
    return is_binary
        
if __name__ == "__main__":
    main()