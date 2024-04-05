import sys
import heapq

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    queue = []
    for _ in range(n):
        x = int(sys.stdin.readline())

        if not x:
            if not queue:
                print(0)
            else:
                print(heapq.heappop(queue))

        else:
            heapq.heappush(queue, x)
