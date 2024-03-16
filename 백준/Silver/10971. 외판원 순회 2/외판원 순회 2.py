import sys

    
def travel(depth, num, hand, price):
    global ans, n, pivot

    if depth == 0:
        if a[hand[-1]][hand[0]] != 0:
            if price > ans and not pivot:
                return

            price += a[hand[-1]][hand[0]]

            if price < ans or pivot:
                ans = price
                pivot = 0
                return

    else:
        for i in range(n):
            if a[num - 1][i] != 0:
                if i not in hand and (a[num-1][i] < ans or pivot):
                    hand.append(i)

                    if depth == n:
                        travel(depth - 1, i + 1, hand, 0)
                    else:
                        travel(depth - 1, i + 1, hand, price + a[num - 1][i])

                    hand.pop()


a = []
ans = 0
pivot = 1
n = int(sys.stdin.readline())

for t in range(n):
    a.append(list(map(int, input().split())))

travel(n, 0, [], 0)

print(ans)
