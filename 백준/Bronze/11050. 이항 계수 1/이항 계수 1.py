import sys

if __name__ == '__main__':
    n, k = map(int, sys.stdin.readline().split())
    temp = n-k
    
    for i in range(2, n):
        n *= i
    
    if k == 0:
        k = 1
    else:
        for i in range(2, k):
            k *= i

    if temp == 0:
        temp = 1
    else:
        for i in range(2, temp):
            temp *= i

    result = n // (k * temp)
    print(result)
