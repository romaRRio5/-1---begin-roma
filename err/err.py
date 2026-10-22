a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
try:
    print(f"{a / b:.1f}")
except ZeroDivisionError:
    print("Делить на ноль нельзя")
