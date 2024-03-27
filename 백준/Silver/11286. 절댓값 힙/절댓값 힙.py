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
                abs_num, real_num = heapq.heappop(queue)
                print(real_num)

        else:
            heapq.heappush(queue, (abs(x), x))
