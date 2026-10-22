n = int(input('введите целое число: '))
total = 0
for i in range(n, 2 * n + 1):
    total += i * i
print(total)
