import Lab3 as l3

def infixToPostfix(expression):
    result = ""
    stack = l3.ArrayStack()
    oper = {None: 0, "+": 1, "-": 1, "*": 2, "/": 2}

    for i in expression:
        if i.isalpha():
            result += i
        elif stack.is_empty() or oper[i] > oper[stack.stackTop()]:
            stack.push(i)
        else:
            while not stack.is_empty():
                a = stack.pop()
                result += a
            stack.push(i)

    while not stack.is_empty():
        a = stack.pop()
        result += a
    return result

exp = "A+B*C-D/E"
postfix = infixToPostfix(exp)
print("Postfix of", exp, "is", postfix)
