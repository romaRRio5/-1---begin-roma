a = float(input("Введите координату A: "))
b = float(input("Введите координату B: "))
c = float(input("Введите координату C: "))
ac = abs(c - a)
bc = abs(c - b)
sum_len = ac + bc
print(f"Длина AC: {ac}")
print(f"Длина BC: {bc}")
print(f"Сумма: {sum_len}")
