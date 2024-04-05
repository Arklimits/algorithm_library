import sys
from collections import deque

read = sys.stdin.readline

n = int(read())
queue = deque()


def program():
    for _ in range(n):
        comm = read().strip()

        if ' ' in comm:
            comm, num = comm.split()
            queue.append(num)

        elif comm == 'pop':
            if queue:
                print(queue.popleft())
            else:
                print(-1)

        elif comm == 'size':
            print(len(queue))

        elif comm == 'empty':
            if len(queue):
                print(0)
            else:
                print(1)

        elif comm == "front":
            if len(queue):
                print(queue[0])
            else:
                print(-1)

        elif comm == "back":
            if len(queue):
                print(queue[-1])
            else:
                print(-1)


program()
