import sys


def dynamic(k):
    dp = [1] + [0 for _ in range(N[k])]

    for i in range(1, 4):
        for j in range(i, N[k]+1):
            p = 0
            for x in range(1, i+1):
                p += dp[j-x]
            dp[j] = p

        # print(i, dp)
    print(dp[N[k]])


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    N = [int(sys.stdin.readline()) for _ in range(T)]

    for t in range(T):
        dynamic(t)
