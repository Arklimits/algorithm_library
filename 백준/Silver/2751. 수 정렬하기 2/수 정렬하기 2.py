import sys

n = int(sys.stdin.readline())

a = sorted(list(map(int, sys.stdin.readlines())))

print('\n'.join(map(str, a)))
