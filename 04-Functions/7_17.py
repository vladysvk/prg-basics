def main():
    print(f("radar"))

def f(palindrome):
    red_backwards = ""
    for i in range(-len(palindrome), 0):
        red_backwards += palindrome[i]
    if red_backwards == palindrome:
        return True
    return False

if __name__ == "__main__":
    main()