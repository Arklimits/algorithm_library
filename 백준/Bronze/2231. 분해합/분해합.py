n = int(input())

for i in range(n):
    text = str(i)
    plus = 0

    for j in text:
        plus += int(j)

    if (i + plus) == n:
        print(i)
        exit()

print(0)
