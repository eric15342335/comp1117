num = []
while True:
    user = input()
    if user == "BYE":
        print("Bye Bye")
        break
    if user == "ADD":
        num.append(int(input()))
    if user == "SHOW":
        print(num)
    if user == "COUNT":
        print(len(num))
    if user == "AVERAGE":
        print(sum(num) / len(num))
