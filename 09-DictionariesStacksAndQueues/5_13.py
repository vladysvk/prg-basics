import queue

def main():
    expression = input("Enter an expression you want to evaluate: ")
    print(RPN(expression))
def RPN(expression):
    stack = queue.LifoQueue()

    expression = expression.split()
    for char in expression:
        if char in "+-*/":
            number2 = stack.get()
            number1 = stack.get()
            if char == "+":
                result = number1 + number2
            elif char == "-":
                result = number1 - number2
            elif char == "*":
                result = number1 * number2
            elif char == "/":
                result = number1 / number2
            stack.put(result)
        elif char == "=":
            return int(stack.get())
        else:
            stack.put(int(char))


if __name__ == "__main__":
    main()