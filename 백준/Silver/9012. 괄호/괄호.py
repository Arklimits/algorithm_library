import sys

read = sys.stdin.readline

n = int(read())

for _ in range(n):
    text = read().strip()
    pivot = 0

    for i in text:
        if i == "(":
            pivot += 1
        elif i == ")":
            pivot -= 1

        if pivot < 0:
            print('NO')
            break

    if pivot == 0:
        print('YES')
    elif pivot < 0:
        continue
    else:
        print('NO')
