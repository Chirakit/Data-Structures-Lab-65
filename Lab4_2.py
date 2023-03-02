from Lab3 import *
def copyStack(s1, s2):
    stack = ArrayStack()
    while s1.is_empty() == False:
        a = s1.pop()
        stack.push(a)

    while s2.is_empty() == False:
        a = s2.pop()

    while stack.is_empty() == False:
        a = stack.pop()
        s1.push(a)
        s2.push(a)

s1 = ArrayStack()
s2 = ArrayStack(); s2.push(15)
copyStack(s1, s2)
s1.printStack()
s2.printStack()
