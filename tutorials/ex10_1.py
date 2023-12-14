def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(int(input())))

assert factorial(0) == 1
assert factorial(1) == 1
assert factorial(5) == 120
