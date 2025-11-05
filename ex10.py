# desenvolver um codigo python que verifica qual dos dois valores é maior - O usuário deve digitar os dois valores

v1 = int(input("Digite o primeiro valor: "))
v2 = int(input("Digite o segundo valor: "))

if v1 > v2:
    print(f"{v1} é maior do que {v2}")
elif v2 > v1:
    print(f"{v2} é maior do que {v1}")
else:
    print("Os valores são iguais.")

