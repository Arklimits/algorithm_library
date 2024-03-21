import sys

read = sys.stdin.readline

n = int(read())
stack = []

for _ in range(n):
    stack.append(int(read()))

high = max(stack)
right = stack.pop()
cnt = 1

for i in reversed(range(n-1)):
    temp = stack.pop()

    if temp > right:
        cnt += 1
        right = temp
    if temp == high:
        break

print(cnt)