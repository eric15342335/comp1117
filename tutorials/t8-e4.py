def func(n, digit):
    # Your implementation
    count = 0
    for i in range(1, n + 1):
        for j in str(i):
            count += str(digit) in j
    return count


n = int(input())
digit = int(input())
print(func(n, digit))
