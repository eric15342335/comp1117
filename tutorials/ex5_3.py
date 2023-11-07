n = int(input())
count = 1
while n-1:
    if n%2:
        n = 3*n+1
    else:
        n = n/2
    count+=1
print(count)
