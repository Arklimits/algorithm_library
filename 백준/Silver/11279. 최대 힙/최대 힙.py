import sys
from queue import PriorityQueue

read = sys.stdin.readline


def program():  # 구동부
    for i in range(N):
        x = int(read())

        if not x:
            if queue.qsize():
                max_val = queue.get()
                print(-max_val)
            else:
                print(0)
        else:
            queue.put(-x)


# 선언부
N = int(read())
queue = PriorityQueue()

program()
