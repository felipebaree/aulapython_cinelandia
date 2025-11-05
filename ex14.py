#desenvolva um codigo pythonque verifique se a temperatura esta frio, agradavel ou calor, siga os valores menor que 18 - frio, entre 18 e 30 - agradavel, maior que 30 calor
temp = float(input("Digite a temperatura atual : "))

if temp < 18:
    print("Está frio.")
elif 18 <= temp <= 30:
    print("O clima está agradável.")
else:
    print("Está calor.")