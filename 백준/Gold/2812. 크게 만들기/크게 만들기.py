import sys
from collections import deque

read = sys.stdin.readline


def program():  # 구동부
    global k
    cnt = 0

    for i in number:
        while len(stack) > 0 and cnt < k and stack[-1] < i:
            stack.pop()
            cnt += 1
        stack.append(i)

    while len(stack) > n - k:
        stack.pop()

    for i in stack:
        print(i, end='')


# 선언부
n, k = map(int, read().split())
number = read().strip()
stack = deque()

program()
