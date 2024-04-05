import sys
from collections import deque


def program():
    text = list(map(str, sys.stdin.readline().strip()))
    explosive = sys.stdin.readline().strip()
    stack = deque()

    explosive = list(reversed(explosive))

    for i in text:
        if i == explosive[0]:
            temp = deque()
            for j in range(1, len(explosive)):
                if stack:
                    if stack[-1] == explosive[j]:
                        temp.append(stack.pop())
                    else:
                        stack += reversed(temp)
                        break
                else:
                    stack += reversed(temp)
                    break
            else:
                continue

        stack.append(i)

    if stack:
        print(''.join(stack))
    else:
        print('FRULA')


if __name__ == '__main__':
    program()
