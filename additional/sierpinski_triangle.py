from turtle import *

speed(0)


def ST(level, size):
    if level == 0:
        forward(size)
        left(120)
    else:
        for i in range(3):
            ST(level - 1, size / 2)
            forward(size / 2)
            left(120)


ST(4, 500)
done()
