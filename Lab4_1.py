import Lab3 as l3

def is_parentheses_matching(expression):
    stack = l3.ArrayStack()
    for i in expression:
        if i == "(":
            stack.push(i)
        elif i == ")":
            if stack.is_empty():
                print("Parentheses in", expression, "are unmatched")
                return False
            else:
                stack.pop()

    if stack.is_empty() == False:
        print("Parentheses in", expression, "are unmatched")
    return stack.is_empty()

str = "((()))"
result = is_parentheses_matching(str)
print(result)
