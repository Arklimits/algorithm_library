import sys


def min_check(start, end):
    dist_min = 2 * 20000 ** 2
    for i in range(start, end - 1):
        for j in range(i + 1, end):
            dist = (arr[i][0] - arr[j][0]) ** 2 + (arr[i][1] - arr[j][1]) ** 2
            dist_min = min(dist_min, dist)
    return dist_min


def travel(start, end):
    size = end - start

    if size < 3:
        return min_check(start, end)

    mid = (start + end) // 2
    left = travel(start, mid)
    right = travel(mid, end)
    half = arr[mid][0]
    check = []

    min_dist = min(left, right)

    for i in range(start, end):
        if (arr[i][0] - half) ** 2 <= min_dist:
            check.append(arr[i])

    check.sort(key=lambda x: x[1])

    for i in range(len(check)):
        now = check[i]
        for j in range(i+1, len(check)):
            compare = check[j]
            if (compare[1] - now[1]) ** 2 >= min_dist:
                break
            dist = (now[0] - compare[0]) ** 2 + (now[1] - compare[1]) ** 2
            min_dist = min(min_dist, dist)

    return min_dist


n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

arr.sort()

print(travel(0, n))
