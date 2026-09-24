a = float(input('Первое значение: '))
b = float(input('Второе значение: '))
c = float(input('Третье значение: '))
temp = a
a = b
b = c
c = temp
print(f"Новое значение A: {a}")
print(f"Новое значение B: {b}")
print(f"Новое значение C: {c}")