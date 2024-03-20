import sys


n = int(sys.stdin.readline())
i = 2

while n >= i:
    if n % i == 0:
        print(i)
        n /= i
    else:
        i += 1

