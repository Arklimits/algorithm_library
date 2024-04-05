import sys
from collections import deque

input = sys.stdin.readline


def program(queue):  # 구동부
    index = 1
    stack = deque()
    square = 0

    stack.append((index, queue.popleft()))
    while queue:
        pivot = queue.popleft()
        index += 1
        if stack[-1][1] < pivot:
            stack.append((index, pivot))
        else:
            while stack and stack[-1][1] >= pivot:
                a, b = stack.pop()
                square = max(b * (index - a), square)
            stack.append((a, pivot))

    while stack:
        a, b = stack.pop()
        square = max(b * (N - a + 1), square)

    print(square)


# 선언부
N = int(input())
QUEUE = []
for _ in range(N):
    QUEUE.append(int(input()))

QUEUE = deque(QUEUE)

program(QUEUE)
