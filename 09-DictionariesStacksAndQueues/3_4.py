import queue

def main():
    number = 18
    print(nat_to_bin(18))

def nat_to_bin(number):
    binary_stack = queue.LifoQueue()

    while number > 0:
        binary_stack.put(number%2)
        number = number//2
    
    binary_number = ""

    while not binary_stack.empty():
        binary_number += str(binary_stack.get())

    return binary_number
if __name__ == "__main__":
    main()