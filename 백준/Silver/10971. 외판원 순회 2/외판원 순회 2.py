import sys


def load(): return sys.stdin.readline()


def travel(depth, start, basket, price):
    global ans, n

    if depth == 0:
        if w[flag.index(n)][flag.index(1)] != 0:
            if price > ans:
                return
            price += w[flag.index(n)][flag.index(1)]
            ans = min(ans, price)

    else:
        for i in range(depth):
            dest = basket[0]
            del basket[0]

            if 0 < w[start][dest] < ans:
                flag[dest] = n - depth + 1
                if depth == n:
                    travel(depth - 1, dest, basket, 0)
                else:
                    travel(depth - 1, dest, basket, price + w[start][dest])

                flag[dest] = 0

            basket.append(dest)


ans = int(1e10)
n = int(load())

flag = [0] * n
arr = [t for t in range(n)]
w = [list(map(int, load().split())) for t in range(n)]

travel(n, 0, arr, 0)

print(ans)
