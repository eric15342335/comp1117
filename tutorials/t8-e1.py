def product(n):
    # Your implementation
    n -= n % 2
    if n == 0:
        return 1
    return n * product(n - 2)


print(product(int(input())))
