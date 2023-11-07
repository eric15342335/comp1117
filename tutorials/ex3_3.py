bmi = float(input()) / float(input()) ** 2
if 30 <= bmi:
    print('Obesity')
elif 25 > bmi:
    print('Other')
else:
    print('Overweight')
