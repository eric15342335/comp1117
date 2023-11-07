s = "the man the boy and the dog"
substring = "the"
pos = s.find(substring, 0)
while pos != -1:
    print(pos, end=" ")
    pos = s.find(substring, pos+len(substring))
