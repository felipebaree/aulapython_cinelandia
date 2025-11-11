#desenvolva um código pyton com while que o usuário digita um numero e o sietema ira mostrar a tabuada deste numero

numero = int(input("Digite um número para ver sua tabuada: "))
i = 1
while i <= 10:
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
    i += 1