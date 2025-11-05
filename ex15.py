nascimento = int(input("Digite o ano de nascimento: "))
sexo = input("Digite o sexo (M ou F): ").upper()
ano = 2025
idade = ano - nascimento
if sexo == "M" and idade >= 18:
    print(f"Você tem {idade} anos e é do sexo masculino. Está APTO.")
else:
    print(f"Você tem {idade} anos e é do sexo {sexo}. NÃO está apto.")