mode, key, text = int(input()), int(input()), list(input().strip('"'))


def rotate(a: str, b: int) -> int:
    if ord(a) == 32:
        return 32
    c = ord(a) + b
    if a.islower():
        if c > 122:
            c = c % 122 + 96
        if c < 97:
            c = 26 + c
    elif a.isupper():
        if c > 90:
            c = c % 90 + 65
        if c < 65:
            c = 26 + c
    return c


if mode == 1:
    for i in text:
        print(chr(rotate(i, key)), end='')
elif mode == 2:
    for i in text:
        print(chr(rotate(i, -key)), end='')
else:
    print("Invalid mode")
