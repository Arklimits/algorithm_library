import sys


def search(depth, num, hand):
    if depth == 0:
        if sum(hand) == 100:
            hand.sort()
            print('\n'.join(map(str, hand)))
            exit(0)
        else:
            return

    for i in range(num, len(arr)):
        hand.append(arr[i])
        search(depth-1, i+1, hand)
        hand.pop()


arr = list(map(int, sys.stdin.readlines()))

search(7, 0, [])
