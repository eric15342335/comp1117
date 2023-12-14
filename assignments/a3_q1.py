number = int(input())
nums = []
while number != -1:
    nums.append(number)
    number = int(input())
target = int(input())
k = int(input())


# Begin of your implementation ------

# End of your implementation ------


def isExist(selected: list, counter, loops: int) -> bool:
    # Begin of your implementation ------
    if loops == 0:  # base case
        # multiply all numbers in selected
        a = 1
        for i in selected:
            a *= i
        if a == target:
            return True  # found a combination
        # returns None by default
    else:
        # print(selected, counter, loops)
        for i in range(counter, len(nums)):  # brute force
            if target % nums[i] == 0:  # check can be included
                n = selected + [nums[i]]  # n: private variable
                if isExist(n, counter + 1, loops - 1):
                    return True  # stop the program
    # End of your implementation ------


if isExist([], 0, k):
    print("Yes")
else:
    print("No")
