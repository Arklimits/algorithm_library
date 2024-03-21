import sys

read = sys.stdin.readline

k = int(read())
stack = []

for _ in range(k):
    temp = int(read())
    if temp:
        stack.append(temp)
    else:
        stack.pop()

print(sum(stack))