a = float(input("Введите координату A: "))
b = float(input("Введите координату B: "))
c = float(input("Введите координату C: "))
ac = abs(c - a)
bc = abs(c - b)
prod = ac * bc
print(f"Произведение длин отрезков AC и BC: {prod}")
