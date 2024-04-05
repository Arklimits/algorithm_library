n = int(input())
a = int(1e7)


def dream(num, depth):
    global a

    if depth > a:
        return

    if num == 1:
        a = min(a, depth)
        return

    if num % 3 == 0:
        dream(num//3, depth+1)
    if num % 2 == 0:
        dream(num//2, depth+1)
    dream(num-1, depth+1)


dream(n, 0)

print(a)
