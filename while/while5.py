n = int(input('введите целое числ: '))
rest = n
k = 0
while rest > 1:
    rest //= 2
    k += 1
print(k)
