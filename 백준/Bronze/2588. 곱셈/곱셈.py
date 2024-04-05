if __name__ == '__main__':
    a = int(input())
    b = int(input())

    i = (b % 10)
    ii = (b % 100)

    print(a * i)
    print(int(a * (ii-i) / 10))
    print(int(a * (b-ii) / 100))
    print(a * b)