#desenvolva um codigo python que verifica se é positivo, negativo ou 0
v = float(input("Digite o valor: "))
if (v > 0):
    print(f"{v} é positivo")
elif (v < 0):
    print(f"{v} é negativo")
else:
    print(f"{v} é zero")
