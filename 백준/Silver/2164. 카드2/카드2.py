import sys
from collections import deque

read = sys.stdin.readline

n = int(read())
queue = deque()
for _ in range(1, n+1):
    queue.append(_)


def program():
    while len(queue) > 1:
        queue.popleft()
        queue.append(queue.popleft())

    print(queue[0])


program()
