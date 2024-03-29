import sys


def dynamic():
    global WEIGHT

    dp = [[0 for _ in range(WN + 1)] for _ in range(WN + 1)]

    for i in range(1, WN + 1):
        for j in range(1, WN + 1):
            if i <= j:
                dp[i][j] = dp[i - 1][j - 1] + WEIGHT[j - 1]
            else:
                if j == 1:
                    dp[i][j] = WEIGHT[i - 2]
                else:
                    dp[i][j] = dp[i - 1][j - 1] + WEIGHT[i - 1]

            if dp[i][j] not in WEIGHT:
                WEIGHT.append(dp[i][j])
    # 
    # for _ in range(WN + 1):
    #     print(dp[_])

    WEIGHT = list(set(WEIGHT))
    WEIGHT.sort()

    for biz in BIZ:
        if biz in WEIGHT:
            print('Y', end=' ')
        else:
            for weight in WEIGHT:
                if biz + weight in WEIGHT:
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
