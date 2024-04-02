import sys


def dynamic(text1, text2):
    if len(text1) > len(text2):
        text1, text2 = text2, text1

    max_length = 0

    j = 0
    for i in range(1, len(text1)+1):
        # print(text1[j:i])
        if text1[j:i] in text2:
            max_length = max(max_length, i-j)
        else:
            j += 1

    print(max_length)


if __name__ == '__main__':
    TEXT1 = sys.stdin.readline().rstrip()
    TEXT2 = sys.stdin.readline().rstrip()

    dynamic(TEXT1, TEXT2)
