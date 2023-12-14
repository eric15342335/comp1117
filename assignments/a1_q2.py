# use of .lower() .upper() is prohibited
name1, name2 = input(), input()
choice1, choice2 = input(f"{name1}'s choice:"), input(f"{name2}'s choice:")
victory = {
    "R": ["S", "s"],
    "S": ["P", "p"],
    "P": ["R", "r"],
    "r": ["S", "s"],
    "s": ["P", "p"],
    "p": ["R", "r"],
}
if choice2 in victory[choice1]:
    print(name1, "wins!")
elif choice1 in victory[choice2]:
    print(name2, "wins!")
else:
    print("Draw!")
