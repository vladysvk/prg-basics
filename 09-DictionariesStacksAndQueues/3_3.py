import queue

expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}" # brackets ok
expression2 = "[(2+3]/4)"                 # brackets not correct
expression3 = "(2-3*4+(5/6)"              # brackets not correct


def brackets_ok(expression):
    correct = False
    stack = queue.LifoQueue()
    for i in expression:
        if i == "[" or i == "{" or i == "(":
            stack.put(i)
        elif i == "]":
            if stack.get() != "[":
                return False
        elif i == "}":
            if stack.get() != "{":
                return False
        elif i == ")":
            if stack.get() != "(":
                return False
            
    return True

if brackets_ok(expression1):
   print("First expression is correct")
else:
   print("First expression is not correct")

if brackets_ok(expression2):
   print("Second expression is correct")
else:
   print("Second expression is not correct")
