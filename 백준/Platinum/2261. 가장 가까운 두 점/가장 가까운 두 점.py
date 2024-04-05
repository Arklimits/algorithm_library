import sys


def min_check(lp, rp):
    dist_min = 2 * 20000 ** 2
    rp -= 1
    if lp < rp:
        dist = (arr[lp][0] - arr[rp][0]) ** 2 + (arr[lp][1] - arr[rp][1]) ** 2
        if dist_min > dist:
            dist_min = dist

    return dist_min


def travel(start, end):
    size = end - start

    if size < 3:
        return min_check(start, end)

    mid = (start + end) // 2
    
    left = travel(start, mid)
    right = travel(mid, end)
    
    check = []

    min_dist = min(left, right)

    for i in range(start, end):
        if (arr[i][0] - arr[mid][0]) ** 2 <= min_dist:
            check.append(arr[i])

    check.sort(key=lambda x: x[1])

    for i in range(len(check)-1):
        now = check[i]
        for j in range(i+1, len(check)):
            comp = check[j]
            if (comp[1] - now[1]) ** 2 >= min_dist:
                break

            dist = (now[0] - comp[0]) ** 2 + (now[1] - comp[1]) ** 2

            if min_dist > dist:
                min_dist = dist

    return min_dist


n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

arr.sort()

print(travel(0, n))
