def z(depth, y, x):
    global count, r, c

    if depth == 0:
        count += (c % 2) + 2 * (r % 2)
        return

    if (r // 2) * 2 >= y + (2 ** depth):
        count += 2 ** (2 * depth + 1)
        z(depth, y + (2 ** depth), x)
    elif (c // 2) * 2 >= x + (2 ** depth):
        count += 2 ** (2 * depth)
        z(depth, y, x + (2 ** depth))
    else:
        z(depth - 1, y, x)


n, r, c = map(int, input().split())

count = 0

z(n-1, 0, 0)

print(count)
