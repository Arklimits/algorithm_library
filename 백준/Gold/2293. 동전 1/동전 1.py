import sys


def dynamic():
    arr = [int(sys.stdin.readline()) for _ in range(N)]
    dp = [1] + [0 for _ in range(K)]

    for i in range(N):
        for j in range(arr[i], K + 1):
            dp[j] = dp[j - arr[i]] + dp[j]

            # print(j, j % arr[i], dp)
    print(dp[K])


if __name__ == '__main__':
    N, K = map(int, sys.stdin.readline().split())

    dynamic()
