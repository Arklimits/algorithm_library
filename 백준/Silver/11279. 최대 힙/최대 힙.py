import sys
import heapq

read = sys.stdin.readline


def program():  # 구동부
    for i in range(N):
        x = int(read())

        if not x:
            if len(queue):
                max_val = heapq.heappop(queue)
                print(-max_val)
            else:
                print(0)
        else:
            heapq.heappush(queue, -x)


# 선언부
N = int(read())
queue = []

program()
