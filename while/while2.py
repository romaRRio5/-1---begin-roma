a = int(input('введите положительное чило А>B: '))
b = int(input('введите положительное числ B: '))
free = a
count = 0
while free >= b:
    free -= b
    count += 1
print(count)
