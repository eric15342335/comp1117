a, b = int(input()), int(input())
if 0 < a < 1000:
    if 1 <= b <= 9:
        c = 0
        for i in range(1, a + 1):
            c += str(i).count(str(b))
        print(c)
    else:
        print("Invalid required digit")
else:
    print("Invalid number")
