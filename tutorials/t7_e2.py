def sqr(x: int) -> int:
    return x ** 2


# print square values between first input and second input (inclusive)
print(list(map(sqr, [i for i in range(int(input()), int(input()) + 1)])))
