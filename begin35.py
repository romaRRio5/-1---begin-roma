V = float(input("V (скорость лодки, км/ч): "))
U = float(input("U (скорость течения, км/ч): "))
T1 = float(input("T1 (время по озеру, ч): "))
T2 = float(input("T2 (время против течения, ч): "))

S = V * T1 + (V - U) * T2

print("Путь S =", S, "км")
