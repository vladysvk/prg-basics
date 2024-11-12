def main():
    print(f("ax15"))
    print(f("book123")) 
    print(f("A2water3")) 
    print(f("qwerty")) 
    print(f(""))

def f(password):
    if len(password) < 6:
        return False 
    letters = ""
    for i in password:
        if i in letters:
            return False
        else:
            letters += i
    return True

if __name__ == "__main__":
    main()