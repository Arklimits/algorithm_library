import sys

read = sys.stdin.readline

text = read()


def check(x):
    if not stack:
        print(0)
        exit()
    elif x == ']' and stack[-1] == '(':
        print(0)
        exit()
    elif x == ')' and stack[-1] == '[':
        print(0)
        exit()


def program():
    p = ''

    res = 0
    val = 1

    for i in text:
        if i == '(':
            stack.append('(')
            val *= 2
        elif i == ')':
            check(i)
            if p == '(':
                res += val
            stack.pop()
            val //= 2
        elif i == '[':
            stack.append('[')
            val *= 3
        elif i == ']':
            check(i)
            if p == '[':
                res += val
            val //= 3
            stack.pop()

        p = i

    if stack:
        print(0)
        exit()

    print(res)


stack = []

program()
