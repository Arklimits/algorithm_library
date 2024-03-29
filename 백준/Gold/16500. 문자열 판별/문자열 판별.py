import sys


def dynamic(arr):
    dp = [1] + [0] * (len(S))

    for i in range(len(S)+1):
        for j in arr:
            # print(f"{j=} {dp=}")
            if i >= len(j) and dp[i - len(j)] and S[i - len(j):i] == j:
                dp[i] = 1

    if dp[len(S)]:
        print(1)
    else:
        print(0)


if __name__ == '__main__':
    S = sys.stdin.readline().rstrip()
    N = int(sys.stdin.readline())
    ARR = []
    for _ in range(N):
        ARR.append(sys.stdin.readline().rstrip())

    dynamic(ARR)
