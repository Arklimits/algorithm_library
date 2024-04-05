import sys

read = sys.stdin.readline

n = int(read())
stack = []

for _ in range(n):
    comm = read().strip()

    if ' ' in comm:
        comm, num = comm.split()
        stack.append(int(num))
    elif comm == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)

    elif comm == 'size':
        print(len(stack))

    elif comm == 'empty':
        if stack:
            print(0)
        else:
            print(1)

    elif comm == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)
