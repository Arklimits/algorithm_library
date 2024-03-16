def check(value, arr):
    length = len(arr)
    for depth in range(1, length + 1):
        if value - depth == arr[length - depth] or value + depth == arr[length - depth]:
            return False
    return True


def queen(now, hand):
    global count

    if now >= n:
        count += 1
        return

    for i in range(n):
        if i not in hand:
            # print(i, hand)
            if check(i, hand):
                hand.append(i)
                queen(now+1, hand)
                hand.pop()


n = int(input())
count = 0

queen(0, [])

print(count)
