n = int(input('введите целое число: '))
product = 1.0
for i in range(1, n + 1):
    product *= (10 + i) / 10
print(product)
