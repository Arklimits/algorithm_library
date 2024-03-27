import sys

text = list(map(str, sys.stdin.readline().strip()))

for i in range(len(text)):
    if 'a' <= text[i] <= 'z':
        text[i] = text[i].upper()
    else:
        text[i] = text[i].lower()

print(''.join(text))
