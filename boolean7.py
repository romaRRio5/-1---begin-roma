a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))
if b > a and b < c:
    print('все ок')
elif b < a and b > c:
    print('все ок')
else:
    print('все плохо')  