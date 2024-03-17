import sys


def load():
    return sys.stdin.readline()


def matrix(arr1, arr2):
    ans = [[0] * n for _ in range(n)]
    arr_temp = [[arr2[j][i] for j in range(n)] for i in range(n)]

    for i in range(n):
        for j in range(n):
            pivot = 0
            for x, y in zip(arr1[i], arr_temp[j]):
                pivot += x * y
            ans[i][j] = pivot % 1000

    return ans


def multiply(arr, jisu):
    global temp

    if jisu == 1:
        return matrix(a, e)

    k = multiply(arr, jisu // 2)

    if jisu % 2:
        return matrix(matrix(k, k), a)
    else:
        return matrix(k, k)


n, b = map(int, load().split())
a = [list(map(int, load().split())) for _ in range(n)]
e = [[0] * n for _ in range(n)]
temp = []

for _ in range(n):
    e[_][_] = 1

result = multiply(a, b)
for r in result:
    print(*r)
