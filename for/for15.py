a = float(input('введите вещественное число: '))
n = int(input('введите целое число: '))
result = 1.0
for _ in range(n):
    result *= a
print(result)
