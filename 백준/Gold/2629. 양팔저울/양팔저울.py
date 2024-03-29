import sys


def dynamic():
    global WEIGHT

    dp = [set() for _ in range(WN + 1)]
    dp[0].add(0)

    for i in range(WN):
        dp[i + 1] = set(dp[i])
        for j in dp[i]:
            dp[i + 1].add(j + WEIGHT[i])

    # print(dp)

    for biz in BIZ:
        if biz in dp[WN]:
            print('Y', end=' ')
        else:
            for weight in dp[WN]:
                if biz + weight in dp[WN]:
                    print('Y', end=' ')
                    break
            else:
                print('N', end=' ')


if __name__ == '__main__':
    WN = int(sys.stdin.readline())
    WEIGHT = list(map(int, sys.stdin.readline().split()))
    BN = int(sys.stdin.readline())
    BIZ = list(map(int, sys.stdin.readline().split()))

    dynamic()
