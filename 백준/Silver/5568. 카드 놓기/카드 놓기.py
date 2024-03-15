def combine(num, pick, on_hand):
    if pick >= k:
        if num not in combination:
            combination.append(num)
        return

    for i in range(len(card)):
        if i not in on_hand:
            on_hand.append(i)
            number = num + card[i]
            combine(number, pick + 1, on_hand)
            on_hand.pop()


n = int(input())
k = int(input())

card = []
combination = []

for _ in range(n):
    card.append(input())

combine("", 0, [])

print(len(combination))
