def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def mult(a, b):
    return a * b

def divi(a, b):
    if b != 0:
       a / b
    else:
       print("valor inválido")

num1= int(input("Digite o primeiro número"))
num2= int(input("Digite o primeiro número"))
x=divi(num1, num2)

print(f"Resultado da operação: {x}")
