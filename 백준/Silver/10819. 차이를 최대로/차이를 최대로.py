import sys


def array_builder(depth, num, hand):
    global max_ans, n

    if depth == 0:
        ans = 0

        for i in range(n - 1):
            ans += abs(a[hand[i]] - a[hand[i + 1]])

        if ans > max_ans:
            max_ans = ans
            return
    else:
        for i in range(n):
            if i not in hand:
                hand.append(i)
                array_builder(depth-1, i+1, hand)
                hand.pop()


max_ans = 0
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

array_builder(n, 0, [])

print(max_ans)
