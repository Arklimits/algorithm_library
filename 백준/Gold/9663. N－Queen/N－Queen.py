def queen(now, hand, handup, handdown):
    global count

    if now >= n:
        count += 1
        return

    for i in range(n):
        if i not in hand:
            if now + i not in handup and now - i not in handdown:
                hand.append(i)
                handup.append(now + i)
                handdown.append(now - i)

                queen(now + 1, hand, handup, handdown)

                hand.pop()
                handup.pop()
                handdown.pop()

    return


n = int(input())
count = 0

queen(0, [], [], [])

print(count)