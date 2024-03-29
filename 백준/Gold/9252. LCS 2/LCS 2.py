import sys


def lcs(text1, text2):
    arr = [['' for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]
    ans = []
    res = 0
    for i in range(len(text1)):
        for j in range(len(text2)):
            if text1[i] == text2[j]:
                arr[i + 1][j + 1] = arr[i][j] + text1[i]
            else:
                if len(arr[i][j+1]) < len(arr[i + 1][j]):
                    arr[i + 1][j + 1] = arr[i + 1][j]
                else:
                    arr[i+1][j+1] = arr[i][j+1]

    # for i in range(len(text1) + 1):
    #     for j in range(len(text2)+ 1):
    #         print("'{0:10}'".format(arr[i][j]), end='')
    #     print()

    res = len(arr[-1][-1])
    print(res)
    if res:
        print(arr[-1][-1])


if __name__ == '__main__':
    TEXT1 = list(map(str, sys.stdin.readline().strip()))
    TEXT2 = list(map(str, sys.stdin.readline().strip()))

    lcs(TEXT1, TEXT2)
