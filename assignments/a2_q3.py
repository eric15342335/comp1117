a = [input()]
while True:
    b = sum(map(lambda x: x**2, map(int, [i for i in str(a[-1])])))
    if b in a:
        print(a[0], "is not a heureux number")
        break
    if b == 1:
        print(a[0], "is a heureux number")
        break
    a += [b]
