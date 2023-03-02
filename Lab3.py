"""Lab03 By Chirakit Marchchalee"""

class ArrayStack:
    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def is_empty(self):
        if len(self.data) == 0:
            return True
        else:
            return False

    def push(self, input_data):
        self.data.append(input_data)
        return self.data

    def pop(self):
        if not self.is_empty():
            x = self.data[-1]
            self.data.pop()
            return x
        else:
            print("Underflow: Cannot pop data from an empty list")
            return None

    def stackTop(self):
        if not self.is_empty():
            return (self.data[self.size()-1])
        else:
            return None

    def printStack(self):
            print(self.data)

#myStack = ArrayStack()
#myStack.push(10); myStack.push(20); myStack.push(30)
#myStack.printStack()
#x = myStack.pop()
#print(x)
#myStack.pop()
#myStack.printStack()
#myStack.pop()
#print(myStack.is_empty())
#myStack.pop()
