a = int(input('число А: '))
b = int(input('число B: '))
product = 1  
for i in range(a, b + 1):
    product *= i
print(product)
