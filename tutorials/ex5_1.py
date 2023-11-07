a = input()
print(['NO','YES'][int(a) == sum(map(lambda x:x**3,map(int,[i for i in a])))])