if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c = int(input())

    abc = a*b*c
    ans = [0] * 10

    for i in str(abc):
        ans[int(i)] += 1

    for i in range(len(ans)):
        print(ans[i])