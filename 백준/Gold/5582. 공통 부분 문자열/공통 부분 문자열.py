import sys


def dynamic(text1, text2):
    dp = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]
    max_length = 0

    for i in range(1, len(text1) + 1):
        for j in range(1, len(text2) + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                max_length = max(max_length, dp[i][j])

    # for i in range(len(text1) + 1):
    #     print(*dp[i])

    print(max_length)


if __name__ == '__main__':
    TEXT1 = list(map(str, sys.stdin.readline().strip()))
    TEXT2 = list(map(str, sys.stdin.readline().strip()))

    dynamic(TEXT1, TEXT2)
