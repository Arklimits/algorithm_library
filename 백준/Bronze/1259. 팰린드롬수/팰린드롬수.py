import sys

if __name__ == '__main__':
    while 1:
        ARR = list(map(int, sys.stdin.readline().strip()))

        if len(ARR) == 1 and ARR[0] == 0:
            break

        for i in range(len(ARR)//2):
            if ARR[i] != ARR[-(i+1)]:
                print('no')
                break
        else:
            print('yes')
