import queue


stack = queue.LifoQueue()
stack.put(2)
stack.put(3)
stack.put(7)
stack.put(4)
stack.put(1)
stack.put(9)
stack.put(8)


first = stack.get()
second = stack.get()

sum = first + second
print(sum)
new_sum = 0
while not stack.empty():
    element = stack.get()
    new_sum += element

print(new_sum)