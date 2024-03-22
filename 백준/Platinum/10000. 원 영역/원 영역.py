import sys
import heapq

read = sys.stdin.readline


def program():  # 구동부
    cnt = N + 1
    stack = []

    for i in range(N):
        end, dist = arr[i]
        start = end - dist
        check = end

        while stack:
            chk_end, chk_dist = heapq.heappop(stack)
            chk_end = -chk_end

            if chk_end <= start:
                heapq.heappush(stack, (-chk_end, chk_dist))
                break
            if chk_end - chk_dist >= start:
                if chk_end != check:
                    continue
                check = chk_end - chk_dist
            if check == start:
                cnt += 1

        heapq.heappush(stack, (-end, dist))

    print(cnt)


# 선언부
N = int(read())
arr = []

for _ in range(N):
    x, r = map(int, input().split())
    arr.append((x+r, r*2))

arr.sort()

program()
