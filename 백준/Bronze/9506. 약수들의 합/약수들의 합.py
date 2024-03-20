while 1:
    n = int(input())
    if n == -1:
        break

    arr = [1]

    for i in range(2, int(n**0.5)+1):
        if not n % i:
            arr.append(i)
            arr.append(n//i)

    arr = list(set(arr))
    arr.sort()

    if sum(arr) == n:
        print(f"{n}", end='')
        for i in range(len(arr)):
            if not i:
                print(' = ', end='')
            else:
                print(' + ', end='')
            print(arr[i], end='')
        print()
    else:
        print(f"{n} is NOT perfect.")