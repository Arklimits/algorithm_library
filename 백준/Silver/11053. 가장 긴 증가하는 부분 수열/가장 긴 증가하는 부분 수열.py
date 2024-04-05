import sys


def dynamic(arr):
    dp = [0 for _ in range(len(arr))]

    for i in range(len(arr)):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    # print(dp)

    print(max(dp)+1)


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    ARR = list(map(int, sys.stdin.readline().split()))

    dynamic(ARR)
