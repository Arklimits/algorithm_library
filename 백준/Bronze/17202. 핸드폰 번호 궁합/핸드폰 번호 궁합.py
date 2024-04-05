import sys


def dynamic(text1, text2):
    dp = [[0 for _ in range(15)] for _ in range(15)]

    for i in range(8):
        dp[i * 2][i * 2] = (int(text1[i]) + int(text2[i])) % 10

    for i in range(7):
        dp[i * 2 + 1][i * 2 + 1] = (int(text1[i + 1]) + int(text2[i])) % 10

    for i in range(13):
        for j in range(14 - i):
            dp[j][j + i + 1] = (dp[j][j + i] + dp[j + 1][j + i + 1]) % 10

    print(str(dp[0][13]) + str(dp[1][14]))


if __name__ == '__main__':
    TEXT1 = sys.stdin.readline().rstrip()
    TEXT2 = sys.stdin.readline().rstrip()

    dynamic(TEXT1, TEXT2)
