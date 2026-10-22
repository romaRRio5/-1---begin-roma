a = int(input('число А: '))
b = int(input('число B: '))
total = 0
for i in range(a, b + 1):
    total += i * i
print(total)
