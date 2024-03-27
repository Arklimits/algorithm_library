import sys
import heapq

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    dic = set()
    out_degree = {}
    arr = {}

    for _ in range(n):
        x, y = sys.stdin.readline().split()

        dic.update({x, y})
        if x not in arr:
            arr[x] = [y]
        else:
            arr[x].append(y)

        if y not in out_degree:
            out_degree[y] = 1
        else:
            out_degree[y] += 1

    # print(dic)
    # print(arr)
    # print(out_degree)

    queue = []
    res = []
    temp = []

    for i in dic:
        if i not in out_degree:
            heapq.heappush(queue, i)

    while queue:
        pivot = heapq.heappop(queue)
        res.append(pivot)
        # print(pivot, queue, res)

        if pivot in arr:
            for i in arr[pivot]:
                out_degree[i] -= 1
                if out_degree[i] <= 0:
                    heapq.heappush(temp, i)

        if not queue:
            if not temp:
                break
            queue = temp
            temp = []

    if len(res) != len(dic):
        print(-1)
        exit()

    for i in res:
        print(i)
