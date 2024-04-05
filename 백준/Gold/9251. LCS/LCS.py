import sys


def lcs(text1, text2):
    arr = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]
    res = 0
    for i in range(len(text1)):
        for j in range(len(text2)):
            if text1[i] == text2[j]:
                arr[i+1][j+1] = arr[i][j] + 1
            else:
                arr[i+1][j+1] = max(arr[i+1][j], arr[i][j+1])

        temp = max(arr[i+1])
        res = max(res, temp)

    print(res)


if __name__ == '__main__':
    TEXT1 = list(map(str, sys.stdin.readline().strip()))
    TEXT2 = list(map(str, sys.stdin.readline().strip()))

    lcs(TEXT1, TEXT2)
