import sys


def dynamic():
    dp = [0 for _ in range(N)]
    maximum = 0
    for i in range(N):
        dp[i] = 1
        for j in range(i):
            if C[i] > C[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1

            if maximum < dp[i]:
                maximum = dp[i]

        # print(dp)

    print(N - maximum)


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    C = [int(sys.stdin.readline()) for _ in range(N)]

    dynamic()
