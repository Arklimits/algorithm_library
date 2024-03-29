import sys


def exchange():
    for coin, count in ARR:
        # print(f"Coin: {coin}, Count: {count}")
        for i in reversed(range(T+1)):
            # print(f"{i=}")
            for j in range(1, count + 1):
                if i < coin * j:
                    break
                DP[i] += DP[i - coin * j]

            # print(DP)

    if DP[T] < int(sys.maxsize):
        print(DP[T])
    else:
        print(0)


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    K = int(sys.stdin.readline())
    ARR = []
    DP = [1] + [0 for _ in range(T)]
    for _ in range(K):
        ARR.append(list(map(int, sys.stdin.readline().split())))

    ARR.sort(key=lambda x: -x[0])

    # print(ARR)

    exchange()
