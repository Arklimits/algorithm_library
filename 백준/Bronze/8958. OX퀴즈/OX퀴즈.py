n = int(input())

for _ in range(n):
    text = input()
    score = 0
    temp = 1
    for i in range(len(text)):
        if text[i] == 'O':
            score += temp
            temp += 1
        else:
            temp = 1

    print(score)
                