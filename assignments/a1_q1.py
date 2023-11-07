time12, apm, gmt = int(input()), input(), input()
apm = {'am': 0, 'pm': 12}[apm]+12*time12//100==12
print("%02d" % (eval("time12//100+apm+24" + gmt) % 24), ':', "%02d" % (time12 % 100), sep='')
