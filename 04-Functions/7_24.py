def main():
    print(f("2 + 3"))
    print(f("3 + 8 + 1"))
    print(f("2 + 3 - 4 + 5 - 0"))

def f(expression):
    return eval(expression)
     
if __name__ == "__main__":
    main()