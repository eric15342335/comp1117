# for base 11-16
hex_string = 'ABCDEF'


def convert_base(_n, _b: int) -> str:
    # n is integer in decimal
    # b is 2 <= b <= 16
    if _n < _b:
        # the last digit
        if _b > 10 and _n > 9:
            # base > 10 requires special handling
            # uses ABCDEF
            return hex_string[_n - 10]
        return str(_n)
    else:
        # not the last digit
        # understanding base conversion:
        return convert_base(_n // _b, _b) + convert_base(_n % _b, _b)


n = int(input())
b = int(input())
print(convert_base(n, b))

assert convert_base(13, 2) == '1101'
assert convert_base(56, 4) == '320'
assert convert_base(1117, 8) == '2135'
assert convert_base(2019, 16) == '7E3'
