from collections import deque
import sys

N = int(sys.stdin.readline())

queue = deque()

for _ in range(N):
    arr = list(map(int, sys.stdin.readline().split()))
    if arr[0] == 1:
        queue.appendleft(arr[1])
    elif arr[0] == 2:
        queue.append(arr[1])
    elif arr[0] == 5:
        print(len(queue))
    elif arr[0] == 6:
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(queue) == 0:
            print(-1)
        elif arr[0] == 3:
            print(queue.popleft())
        elif arr[0] == 4:
            print(queue.pop())
        elif arr[0] == 7:
            print(queue[0])
        elif arr[0] == 8:
            print(queue[-1])
