if __name__ == '__main__':
    x, y, w, h = map(int, input().split())

    r = w - x
    u = h - y

    print(min(x, y, r, u))
