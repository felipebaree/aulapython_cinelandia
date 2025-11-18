def dividir(a, b):
    try:
        # TESTE
        resultado = a / b
    except ZeroDivisionError:
        # ERRO
        print("Erro: divisão por zero não é permitida!")
    except ValueError:
        print("Erro: valor inválido informado!")
    else:
        # EXECUTAR QUANDO NÃO HOUVER ERRO
        print(f"Resultado da divisão: {resultado}")
    finally:
        # EXECUTAR SEMPRE
        print("Operação finalizada (com ou sem erro).")

# Programa principal
try:
    num1 = float(input("Digite o numerador: "))
    num2 = float(input("Digite o denominador: "))
    dividir(num1, num2)
except ValueError:
    print("Você deve digitar apenas números!")