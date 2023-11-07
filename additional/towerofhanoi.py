def move(n:int, a,b,c:list)->None:
    # for n==1, a,b,c means source,buffer,destination respectively
    # base case
    if n==1:
        print(f"move from {a} to {c}")
        # a.pop(0) removes&returns a[0]
        # list.insert(a,b)  inserts b after position a
        c.insert(0,a.pop(0))
    else:
        # move n-1 from a to b
        move(n-1,a,c,b)
        # move 1 from a to c
        move(1,a,b,c)
        # move n-1 from b to c
        move(n-1,b,a,c)

# initialization
a,b,c = [],[],[]
# how many plates in a?
n = int(input())
# e.g. for n=5, a=[1,2,3,4,5], a[0] is the top element
for i in range(1,n+1): a.append(i)
move(n,a,b,c)
# print the result
print(a,b,c)
