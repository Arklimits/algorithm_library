def queen(now, basket):
    global count

    if now >= n:
        count += 1
        return

    for i in range(n - now):
        pivot = basket[0]
        basket.remove(pivot)

        if not hand[pivot]:
            if not up[now + pivot] and not down[now - pivot]:
                hand[pivot] = 1
                up[now + pivot] = down[now - pivot] = 1

                queen(now + 1, basket)

                hand[pivot] = 0
                up[now + pivot] = down[now - pivot] = 0

        basket.append(pivot)

    return


n = int(input())
count = 0

hand = [0] * n
up = [0] * n * 2
down = [0] * n * 2

arr = [i for i in range(n)]

queen(0, arr)

print(count)