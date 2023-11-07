frag, frag_n, frag2, frag2_n = 0, 0, 0, 0
a = []

while True:
    b = int(input())
    if b == 0:
        break
    a += [b]

for i in a:
    if i == frag2:
        frag2_n += 1
    else:
        frag2 = i
        frag2_n = 1
    if frag2_n > frag_n:
        frag = frag2
        frag_n = frag2_n

print(frag_n)
