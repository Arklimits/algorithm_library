n, b = input().split()
b = int(b)
arr = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
result = 0

for i, j in zip(n, range(len(n))):
    result += arr.index(i)*b**(len(n)-j-1)

print(result)
