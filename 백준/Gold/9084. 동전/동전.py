import sys


def exchange():
    for coin in ARR:
        # print(f"Coin: {coin}")
        for i in range(1, M + 1):
            # print(f"{i=}")
            if i >= coin:
                DP[i] += DP[i - coin]
            # print(DP)
    print(DP[M])
    # if DP[T] < int(sys.maxsize):
    #     print(DP[T])
    # else:
    #     print(0)


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    for _ in range(T):
        K = int(sys.stdin.readline())
        ARR = list(map(int, sys.stdin.readline().split()))
        M = int(sys.stdin.readline())
        DP = [1] + [0 for _ in range(M)]

        ARR.sort(reverse=True)

        exchange()
