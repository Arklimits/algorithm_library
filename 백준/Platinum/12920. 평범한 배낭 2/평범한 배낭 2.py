import sys


def dynamic(arr):
    n = len(arr)

    dp = [[0 for _ in range(K + 1)] for _ in range(n + 1)]
    arr.sort(reverse=True)
    arr.insert(0, (0, 0, 0))

    for i in range(1, n + 1):
        for j in range(1, K + 1):
            if j < arr[i][1]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(arr[i][2] + dp[i - 1][j - arr[i][1]], dp[i - 1][j])

    # for _ in range(N + 1):
    #     print(*dp[_])

    print(dp[n][K])


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

    if not len(ARR):
        print(0)
        exit()

    dynamic(ARR)
