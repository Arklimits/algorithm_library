import sys
from collections import deque

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    queue = deque()

    for _ in range(n):
        comm = sys.stdin.readline().strip()

        if 'push' in comm:
            text, num = comm.split()
            queue.append(int(num))
        elif comm == 'pop':
            if queue:
                print(queue.popleft())
            else:
                print(-1)
        elif comm == 'size':
            print(len(queue))
        elif comm == 'empty':
            if queue:
                print(0)
            else:
                print(1)
        elif comm == 'front':
            if queue:
                print(queue[0])
            else:
                print(-1)
        elif comm == 'back':
            if queue:
                print(queue[-1])
            else:
                print(-1)
