# Your implementation
# Please enter your code below
def readList():
    bruh = []
    while True:
        user = int(input())
        if user == 0:
            break
        bruh.append(user)
    return bruh


def calSum(a: list) -> int:
    temp = 0
    for b in a:
        temp += b
    return temp



# Given code
# Please do not change the code below
myList = readList()
sum = calSum(myList)
print(sum)