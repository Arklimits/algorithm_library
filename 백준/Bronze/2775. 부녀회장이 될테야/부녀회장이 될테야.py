import sys


def dynamic(k, n):
    dp = [[0 for _ in range(n + 1)] for _ in range(k + 1)]

    for i in range(1, n + 1):
        dp[0][i] = i

    for i in range(1, k + 1):
        for j in range(1, n + 1):
            for h in range(1, j + 1):
                dp[i][j] += dp[i - 1][h]

    print(dp[k][n])


if __name__ == '__main__':
    T = int(sys.stdin.readline())

    for _ in range(T):
        K = int(sys.stdin.readline())
        N = int(sys.stdin.readline())

        dynamic(K, N)
