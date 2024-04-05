import sys


def dynamic():
    limit = int((N * 2) ** 0.5) + 1
    dp = [[int(sys.maxsize) for _ in range(limit + 1)] for _ in range(N + 1)]
    dp[1][0] = 0

    for i in range(2, N + 1):
        if i in STONE:
            continue
        for j in range(1, limit):
            dp[i][j] = min(dp[i-j][j-1], dp[i-j][j], dp[i-j][j+1]) + 1

    # for y in range(N+1):
    #     for x in range(limit+1):
    #         print(dp[y][x] if dp[y][x] < 1e9 else 'X', end=' ')
    #     print()

    if min(dp[N]) == int(sys.maxsize):
        print(-1)
    else:
        print(min(dp[N]))


if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().split())
    STONE = set()
    for _ in range(M):
        STONE.add(int(sys.stdin.readline()))

    dynamic()
