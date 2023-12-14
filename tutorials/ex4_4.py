# perfect number
def factors(n: int) -> list:
    # return a list containing all the factors of n
    a = []
    for i in range(1, n // 2 + 1):
        # no remainder -> factor
        if n % i == 0:
            a += [i]
    return a


while True:
    # enter number
    num = int(input())
    # sum all the factors and compare it to the number
    # to check whether it is a perfect number
    print(sum(factors(num)) == num)
    # continue input? Y/N
    match = input()
    if match == "Y":
        continue
    else:
        break
