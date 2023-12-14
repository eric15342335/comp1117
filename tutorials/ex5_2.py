head, feet = int(input()), int(input())
# for-loop(s) must be used
if feet > head * 2:
    chicken = head
    for i in range(head, 1, -1):
        if chicken * 2 + (head - chicken) * 4 == feet:
            break
        chicken -= 1
    print(chicken)
    print(head - chicken)
else:
    print("ERROR")
