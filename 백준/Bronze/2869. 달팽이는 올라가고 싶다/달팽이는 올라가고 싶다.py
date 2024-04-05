a, b, v = map(int, input().split())

time = int((v - b) / (a - b))
remain = (v - b) % (a - b)

if remain > 0:
    ans = time + 1
else:
    ans = time

print(ans)