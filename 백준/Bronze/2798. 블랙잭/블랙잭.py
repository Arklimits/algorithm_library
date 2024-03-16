import sys


def blackjack(depth, num, hand):
    global m, card_max

    if depth == 0:
        if sum(hand) == m:
            hand.sort()
            print(sum(hand))
            exit(0)
        elif m > sum(hand) >= card_max:
            card_max = sum(hand)

        return


    for i in range(num, len(arr)):
        if num < m and sum(hand) < m:
            hand.append(arr[i])
            blackjack(depth-1, i+1, hand)
            hand.pop()


card_max = 0
n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

blackjack(3, 0, [])

print(card_max)
