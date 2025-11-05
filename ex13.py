#desenvolva um codigo python que leia 3 valores e mostre qual o maior
v1 = float(input("Digite o valor: "))
v2 = float(input("Digite o valor: "))
v3 = float(input("Digite o valor: "))
if v1 > v2 and v1 > v3:
    print(f"O maior valor é {v1}")
elif v2 > v1 and v2 > v3:
    print(f"O maior valor é {v2}")
elif v3 > v1 and v3 > v2:
    print(f"O maior valor é {v3}")
else:
    print("Os valores são iguais.")