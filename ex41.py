def maior_numero(a, b):
    if a > b:
        return a
    else:
        return b


num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

resultado = maior_numero(num1, num2)

print(f"O maior número é: {resultado}")
