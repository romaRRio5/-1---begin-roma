V1 = float(input("V1 (скорость первого, км/ч): "))
V2 = float(input("V2 (скорость второго, км/ч): "))
S = float(input("S (начальное расстояние, км): "))
T = float(input("T (время, ч): "))

result = S + (V1 + V2) * T

print("Расстояние через T часов:", result, "км")
