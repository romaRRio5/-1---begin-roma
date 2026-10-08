a = int(input('Введите целое число: '))
b=a
if a > 0: 
    b+=1 
    print(b)
elif a == 0:
    print('число не подходит')
else:
    a-=2 
    print(a)