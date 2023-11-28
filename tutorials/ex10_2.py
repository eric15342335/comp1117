def combination(n, r: int) -> int:
    # recursive implementation of nCr
    # nCr = (n-1)C(r-1) + (n-1)Cr
    # nC0 = nCn = 1, nCr = 0 if r > n
    if r == 0 or n == r:
        return 1
    if r > n:
        # should have raised error but the question didn't ask for it
        return 0
    return combination(n - 1, r - 1) + combination(n - 1, r)


print(combination(int(input()), int(input())))

assert combination(6, 3) == 20
assert combination(8, 1) == 8
