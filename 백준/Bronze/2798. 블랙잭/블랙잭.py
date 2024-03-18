import sys


def escape(cards):
    print(cards)
    exit(0)
    
    
def blackjack(depth, num, hand):
    global m, card_max
    cards = sum(hand)
    if cards > m:
        return

    if depth == 0:
        if cards == m:
            escape(cards)
        elif m > cards >= card_max:
            card_max = cards

        return

    for i in range(num, len(arr)):
        if arr[i] > m:
            escape(cards)

        hand.append(arr[i])
        blackjack(depth-1, i+1, hand)
        hand.pop()


card_max = 0
n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

arr.sort()

blackjack(3, 0, [])

print(card_max)
