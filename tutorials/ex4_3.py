user = int(input())
sum_of = user
min_of = user
while True:
    user = int(input())
    sum_of += user
    if user == 0:
        break
    if min_of > user:
        min_of = user

print("sum =", sum_of)
print("min =", min_of)
