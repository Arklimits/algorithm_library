import sys


def dynamic(arr):
    dp = [0 for _ in range(K + 1)]
    arr.sort(reverse=True)

    for v, i, j in arr:
        for k in range(K, i-1, -1):
            dp[k] = max(dp[k - i] + j, dp[k])

            # print(*dp)

    print(dp[K])


if __name__ == '__main__':
    N, K = map(int, sys.stdin.readline().split())
    ARR = []
    for _ in range(N):
        a, b, c = map(int, sys.stdin.readline().split())

        t = 1
        while c > 0:
            m = min(t, c)
            ARR.append((b / a, a * m, b * m))
            c -= t
            t *= 2

    # print(ARR)

    dynamic(ARR)
