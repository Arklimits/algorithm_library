import sys


def greedy(pay):
    money = 1000 - pay
    coin = [500, 100, 50, 10, 5, 1]
    count = 0

    for i in range(6):
        if money >= coin[i]:
            count += money // coin[i]
            money %= coin[i]

    print(count)


if __name__ == '__main__':
    PAY = int(sys.stdin.readline())

    greedy(PAY)
