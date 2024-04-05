import sys


read = sys.stdin.readline


def solve():
    result_1 = result_3 = 0
    for i in range(1, n+1):
        result_1 += i
        result_3 += i**3

    print(result_1)
    print(result_1**2)
    print(result_3)


n = int(read())

solve()
