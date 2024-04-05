import sys


def dynamic(arr):
    dp = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(1, N):
        for j in range(N):
            if i + j >= N:
                break

            dp[j][i + j] = int(sys.maxsize)

            for k in range(j, i + j):
                dp[j][i + j] = min(dp[j][i + j], dp[j][k] + dp[k + 1][i + j] + arr[j][0] * arr[k][1] * arr[i + j][1])

                # print(f"{j=} {i=} {k=}")
                # for x in range(N):
                #     print(*dp[x])

    print(dp[0][N-1])


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    ARR = []
    for _ in range(N):
        ARR.append(list(map(int, sys.stdin.readline().split())))

    if N == 1:
        print(0)
    elif N < 3:
        print(ARR[0][0] * ARR[0][1] * ARR[1][1])
    else:
        dynamic(ARR)
