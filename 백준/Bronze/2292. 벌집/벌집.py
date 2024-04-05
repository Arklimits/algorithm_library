import sys

read = sys.stdin.readline

n = int(read())
p = 1
i = 1

while 1:
    if p >= n:
        print(i)
        break
    else:
        p += i * 6
        i += 1
