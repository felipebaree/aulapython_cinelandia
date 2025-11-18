try:
    n1 = float(input("Primeiro número: "))
    n2 = float(input("Segundo número: "))
    op = input("Operação (+, -, x, /): ")

    match op:
        case '+':
            resultado = n1 + n2
        case '-':
            resultado = n1 - n2
        case 'x' | 'X':
            resultado = n1 * n2
        case '/':
            resultado = n1 / n2   # Vai gerar erro automático se n2 for zero
        case _:
            raise ValueError("Operação inválida.")

except ZeroDivisionError:
    print("Erro: divisão por zero!")
except ValueError as e:
    print("Erro:", e)
else:
    print("Resultado:", resultado)
finally:
    print("Fim do programa.")