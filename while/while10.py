n = int(input('введите целое число: '))
power = 1
k = 0
while power * 3 < n:
    power *= 3
    k += 1
print(k)
