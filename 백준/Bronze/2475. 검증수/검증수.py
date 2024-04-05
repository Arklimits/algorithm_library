arr = list(map(int, input().split()))

result = 0

for i in arr:
    result += i**2
result %= 10

print(result)