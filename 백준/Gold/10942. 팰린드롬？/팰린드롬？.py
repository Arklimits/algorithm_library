import sys


def dynamic():
    dp = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        dp[i][i] = 1

    for i in range(N - 1):
        if ARR[i] == ARR[i + 1]:
            dp[i][i + 1] = 1
        else:
            dp[i][i + 1] = 0

    for i in range(N - 2):
        for j in range(N - 2 - i):
            k = j + 2 + i
            if ARR[j] == ARR[k] and dp[j + 1][k - 1] == 1:
                dp[j][k] = 1

    # for i in range(N):
    #     print(dp[i])

    for _ in range(M):
        i, k = list(map(int, sys.stdin.readline().split()))
        print(dp[i-1][k-1])


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    ARR = list(map(int, sys.stdin.readline().split()))
    M = int(sys.stdin.readline())

    dynamic()
