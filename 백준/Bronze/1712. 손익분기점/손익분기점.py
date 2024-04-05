import sys


a, b, c = map(int, input().split())

if c <= b:
    print(-1)
    exit()

start, end = 0, sys.maxsize

while start <= end:
    result = (start + end) // 2
    if (c - b) * result == a:
        result += 1
        break

    elif (c - b) * result < a:
        start = result + 1
    else:
        end = result - 1

if (c - b) * result < a:
    result += 1

print(result)