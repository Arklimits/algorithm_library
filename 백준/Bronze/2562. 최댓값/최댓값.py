if __name__ == '__main__':
    A = []
    for i in range(9):
        A.append(int(input()))

    A_MAX = max(A)
    print(A_MAX)
    print(A.index(A_MAX) + 1)