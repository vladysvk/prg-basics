import queue

def main():
    string = input("Enter a word: ")
    print(reverse(string))



def reverse(string):
    stack = queue.LifoQueue()

    for char in string:
        stack.put(char)

    new_string = ""
    while not stack.empty():
        new_string += stack.get()
    
    return new_string



if __name__ == "__main__":
    main()