
def evaluate(val, exp):
    stack = []
    for c in exp:
        if c == '+':
            a = stack.pop()
            b = stack.pop()
            stack.append(a or b)
        elif c == '*':
            a = stack.pop()
            b = stack.pop()
            stack.append(a and b)
        elif c== '-':
            a = stack.pop()
            stack.append(not a)
#            stack.append('F' if not a else 'T')
#            stack.append(not a ? 'F' : 'T')
        else:
            stack.append(val[ord(c) - ord('A')] == 'T')
#        print(stack)

    return stack.pop()

if __name__ == "__main__":
    num = int(input()) # number of variables
    values = list(input().split(' '))
    expression = list(input().split(' '))
    ret = evaluate(values, expression)
    if ret:
        print('T')
    else:
        print('F')

