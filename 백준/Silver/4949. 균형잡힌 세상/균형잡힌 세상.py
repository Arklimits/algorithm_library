import sys

while 1:
    s = input()

    if s == '.':
        break

    stack = []

    for i in s:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if len(stack) == 0:
                print('no')
                break
            else:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    print('no')
                    break
        elif i == ']':
            if len(stack) == 0:
                print('no')
                break
            else:
                if stack[-1] == '[':
                    stack.pop()
                else:
                    print('no')
                    break
    else:
        if len(stack) == 0:
            print('yes')
        else:
            print('no')
