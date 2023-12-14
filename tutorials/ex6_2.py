for i in range(1, int(input()) + 1):
    for j in range(i, 0, -1):
        print(1 * (j % 2 == 0), end=" ")
    print()
