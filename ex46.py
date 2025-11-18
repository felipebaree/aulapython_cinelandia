def calcular_media():
    try:
        n1 = float(input("Digite a primeira nota: "))
        n2 = float(input("Digite a segunda nota: "))
        media = (n1 + n2) / 2
    except ValueError:
        print("Erro: digite apenas números válidos!")
    else:
        print(f"Média calculada: {media:.2f}")
    finally:
        print("Fim do cálculo de média.")

calcular_media()