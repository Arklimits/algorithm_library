t = int(input())

for i in range(t):
    r, s = map(str, input().split())
    for k in range(len(s)):
        for j in range(int(r)):
            print(s[k], end='')
    print()
