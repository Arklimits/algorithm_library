import sys


read = sys.stdin.readline


def solve():
    for i in range(m):
        now = line[i]
        start, end = 0, n - 1
        
        # 범위 확인
        if dot[end] < now[0] or dot[start] > now[1]:
            print(0)
            continue

        # 좌측 확인
        while start <= end:
            mid = (start + end) // 2
            if dot[mid] <= now[0]:
                start = mid + 1
            else:
                end = mid - 1

        if end < 0:
            end = 0
        left = end

        # 우측 확인
        start, end = left + 1, n - 1
        while start <= end:
            mid = (start + end) // 2
            if dot[mid] < now[1]:
                start = mid + 1
            else:
                end = mid - 1

        if start > n-1:
            start = n-1
        right = start

        # 범위 확정
        if dot[left] < now[0]:
            left += 1
        if dot[right] > now[1]:
            right -= 1

        print(right-left+1)


line = []
n, m = map(int, read().split())
dot = list(map(int, read().split()))
for _ in range(m):
    line.append(list(map(int, read().split())))

dot.sort()

solve()