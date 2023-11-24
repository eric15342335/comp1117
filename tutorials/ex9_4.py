card = input().replace(" ", "")
a = 0
for i in card[-3::-2]:
    a += int(i)
for i in card[-2::-2]:
    a += int(i) * 2 % 10 + int(i) * 2 // 10
print(["Invalid", "Valid"][10 - a % 10 == int(card[-1])])
# remember to convert string to integer for comparison
