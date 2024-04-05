import sys
import heapq


def calculate():
    for _ in range(n):
        queue1 = []
        queue2 = []
        x = int(sys.stdin.readline())
        id_check = [1] * x

        for i in range(x):
            comm, num = sys.stdin.readline().split()
            num = int(num)

            if comm == 'I':
                heapq.heappush(queue1, (-num, i))
                heapq.heappush(queue2, (num, i))
            else:
                if num == 1:
                    if queue1:
                        temp = heapq.heappop(queue1)
                        id_check[temp[1]] = 0
                else:
                    if queue2:
                        temp = heapq.heappop(queue2)
                        id_check[temp[1]] = 0

            while queue1 and not id_check[queue1[0][1]]:
                heapq.heappop(queue1)
            while queue2 and not id_check[queue2[0][1]]:
                heapq.heappop(queue2)

        if queue1 and queue2:
            num1, i = heapq.heappop(queue1)
            num2, j = heapq.heappop(queue2)
            print(-num1, num2)
        else:
            print('EMPTY')


if __name__ == '__main__':
    n = int(sys.stdin.readline())

    calculate()
