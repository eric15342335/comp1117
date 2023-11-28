def ackermann(m, n: int) -> int:
    # implement ackermann function by recursive function calls
    # A(m,n) = n+1 if m = 0
    if m == 0:
        return n + 1
    # A(m,n) = A(m-1,1) if m > 0 and n = 0
    if m > 0 and n == 0:
        return ackermann(m - 1, 1)
    # A(m,n) = A(m-1,A(m,n-1)) if m > 0 and n > 0
    if m > 0 and n > 0:
        return ackermann(m - 1, ackermann(m, n - 1))


print(ackermann(int(input()), int(input())))

assert ackermann(1, 2) == 4
assert ackermann(4, 0) == 13
