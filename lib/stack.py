
def is_balanced(expression):
    stack = []
    bracket = {')': '(', ']': '[', '}': '{'}

    for char in expression:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack or stack[-1] != bracket[char]:
                return False
            stack.pop()

    return not stack

print(is_balanced("([]{()})")) 
print(is_balanced("([{)})"))   
print(is_balanced("(){}["))    

print('_'*60)