def multiply(a, b):
    # Your implementation
    if b == 1:
        return a
    if b == 0:
        return 0
    return multiply(a, b - 1) + a

a = int(input())
b = int(input())
print(multiply(a, b))
