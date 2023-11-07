n = list(input())
while len(n)>1:
    if n[0]==n[-1]:
        n.pop(0)
        n.pop(-1)
    else:
        break
print(['YES','NO'][len(n)>1])
