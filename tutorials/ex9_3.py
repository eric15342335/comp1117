x = dict()
for i in input():
    x[i] = x.get(i, 0) + 1
    # using get method to initialize x=0
print(x)
