def even_only(x: int) -> bool:
    return not (x % 2)


print(list(filter(even_only, [i for i in range(int(input()), int(input()) + 1)])))
