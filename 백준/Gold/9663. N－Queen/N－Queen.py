def queen(now, hand, handup, handdown, basket):
    global count

    if now >= n:
        count += 1
        return

    for i in range(len(basket)):
        pivot = basket[0]
        basket.remove(pivot)
        
        if pivot not in hand:
            if now + pivot not in handup and now - pivot not in handdown:
                hand.append(pivot)
                handup.append(now + pivot)
                handdown.append(now - pivot)

                queen(now + 1, hand, handup, handdown, basket)

                hand.pop()
                handup.pop()
                handdown.pop()
                
        basket.append(pivot)

    return


n = int(input())
count = 0

arr = [i for i in range(n)]

queen(0, [], [], [], arr)

print(count)