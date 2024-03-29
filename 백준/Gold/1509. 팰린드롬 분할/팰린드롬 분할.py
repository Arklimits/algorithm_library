import sys


def dynamic(text):
    n = len(text)
    dp = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        dp[i][i] = 1

    for i in range(n - 1):
        if text[i] == text[i + 1]:
            dp[i][i + 1] = 1

    for i in range(n):
        for j in range(n - 2 - i):
            k = j + 2 + i
            if text[j] == text[k] and dp[j + 1][k - 1] == 1:
                dp[j][k] = 1

    # for i in range(n):
        # print(*dp[i])

    pp = [2500 for _ in range(n + 1)]
    pp[-1] = 0

    for end in range(n):
        for start in range(end + 1):
            # print(f"{start=} {end=} {pp=}")
            if dp[start][end]:
                pp[end] = min(pp[end], pp[start - 1] + 1)
            else:
                pp[end] = min(pp[end], pp[end - 1] + 1)

    print(pp[n - 1])


if __name__ == '__main__':
    TEXT = list(map(str, sys.stdin.readline().strip()))

    dynamic(TEXT)
