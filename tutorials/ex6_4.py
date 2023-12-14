# Your implementation
# Please enter your code below
def readSet():
    bruh = set()
    while True:
        user = int(input())
        if user == 0:
            break
        bruh.add(user)
    return bruh


def findNo(a: set, b: int) -> bool:
    return b in a


# Given code
# Please do not change the code below
mySet = readSet()
number = int(input("Find number? "))
print(findNo(mySet, number))
