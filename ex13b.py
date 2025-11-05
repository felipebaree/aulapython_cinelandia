# Programa que lê 3 valores e mostra qual é o maior (considerando empates)

v1 = float(input("Digite o primeiro valor: "))
v2 = float(input("Digite o segundo valor: "))
v3 = float(input("Digite o terceiro valor: "))

if v1 == v2 == v3:
    print("Todos os valores são iguais.")
elif v1 == v2 and v1 > v3:
    print(f"O primeiro ({v1}) e o segundo ({v2}) são iguais e maiores que o terceiro ({v3}).")
elif v1 == v3 and v1 > v2:
    print(f"O primeiro ({v1}) e o terceiro ({v3}) são iguais e maiores que o segundo ({v2}).")
elif v2 == v3 and v2 > v1:
    print(f"O segundo ({v2}) e o terceiro ({v3}) são iguais e maiores que o primeiro ({v1}).")
else:
    # aqui é o caso normal: todos diferentes
    if v1 > v2 and v1 > v3:
        print(f"O maior valor é {v1}")
    elif v2 > v1 and v2 > v3:
        print(f"O maior valor é {v2}")
    else:
        print(f"O maior valor é {v3}")