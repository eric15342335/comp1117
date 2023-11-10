user = input()


def is_pal(s: str) -> bool:
    return s == s[::-1]


print(is_pal(user))
