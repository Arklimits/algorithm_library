w, h = map(int, input().split())

n = int(input())

x = [0, w]
y = [0, h]

for _ in range(n):
    direction, cut = map(int, input().split())

    if direction:
        x.append(cut)
    else:
        y.append(cut)

x.sort()
y.sort()

max_x = max_y = 0

for i in range(len(x)-1):
    if x[i+1] - x[i] > max_x:
        max_x = x[i+1] - x[i]

for i in range(len(y)-1):
    if y[i+1] - y[i] > max_y:
        max_y = y[i+1] - y[i]

print(max_x * max_y)