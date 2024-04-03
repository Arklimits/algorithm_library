import sys


def greedy(n, text):
    alpha = {}
    ans = 0
    num = 9

    for i in text:
        x = len(i) - 1
        for j in i:
            if j in alpha:
                alpha[j] += 10 ** x
            else:
                alpha[j] = 10 ** x
            x -= 1

    alpha = sorted(alpha.values(), reverse=True)

    for i in alpha:
        ans += i * num
        num -= 1

    print(ans)


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    TEXT = [sys.stdin.readline().rstrip() for i in range(N)]

    greedy(N, TEXT)
