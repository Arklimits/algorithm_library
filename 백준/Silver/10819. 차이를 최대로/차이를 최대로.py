import sys


def array_builder(depth, hand, basket):
    global max_ans, n

    if depth == 0:
        ans = 0

        for i in range(n - 1):
            ans += abs(a[hand[i]] - a[hand[i + 1]])

        if ans > max_ans:
            max_ans = ans

        return
    else:
        for _ in range(depth):
            temp = basket[0]
            del basket[0]
            hand.append(temp)

            array_builder(depth-1, hand, basket)

            hand.pop()
            basket.append(temp)


max_ans = 0
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
arr = [t for t in range(n)]

array_builder(n, [], arr)

print(max_ans)
