import sys


def program(arr, k):
    ans = 0
    for coin in arr:
        ans += k // coin
        k %= coin
        if k <= 0:
            break

    print(ans)


# 선언부
N, K = map(int, sys.stdin.readline().split())
ARR = []
for _ in range(N):
    temp = int(sys.stdin.readline())
    if temp <= K:
        ARR.append(temp)
    else:
        break

ARR.sort(reverse=True)

program(ARR, K)
