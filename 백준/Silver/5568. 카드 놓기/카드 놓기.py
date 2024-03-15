n = int(input())
k = int(input())
card = []
combination = []
count = 0

for i in range(n):
    card.append(int(input()))

if k == 2:
    for i in range(len(card)):
        for j in range(len(card)):
            if j == i:
                continue
            temp = int(str(card[i]) + str(card[j]))
            if temp not in combination:
                combination.append(temp)
                count += 1
elif k == 3:
    for i in range(len(card)):
        for j in range(len(card)):
            if j == i:
                continue
            for k in range(len(card)):
                if k == i or k == j:
                    continue
                temp = int(str(card[i]) + str(card[j]) + str(card[k]))
                if temp not in combination:
                    combination.append(temp)
                    count += 1
else:
    for i in range(len(card)):
        for j in range(len(card)):
            if j == i:
                continue
            for k in range(len(card)):
                if k == i or k == j:
                    continue
                for m in range(len(card)):
                    if m == i or m == j or m == k:
                        continue
                    temp = int(str(card[i]) + str(card[j]) + str(card[k]) + str(card[m]))
                    if temp not in combination:
                        combination.append(temp)
                        count += 1

print(count)
