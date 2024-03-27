import sys

text = list(map(str, sys.stdin.readline().strip()))
res = 0

if text[0] == 'A':
    res = 4.0
elif text[0] == 'B':
    res = 3.0
elif text[0] == 'C':
    res = 2.0
elif text[0] == 'D':
    res = 1.0
else:
    print(0.0)
    exit()

if text[1] == '+':
    res += 0.3
elif text[1] == '-':
    res -= 0.3

print(res)
