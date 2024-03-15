import math

arr = [0] * 10001
arr[2] = arr[3] = 1

def prime_list(num):
    for token in range(2, int(math.sqrt(num))+1):
        if num % token == 0:
            return

    arr[num] = 1


if __name__ == '__main__':
    for i in range(2, 10001):
        prime_list(i)

    t = int(input())

    for _ in range(t):
        n = int(input())

        key1 = key2 = n // 2

        for _ in range(n // 2):
            if arr[key1] and arr[key2]:
                print(key1, key2)
                break
            else:
                key1 -= 1
                key2 += 1

