#desenvolva um codigo python que verifique se digitou m ou f, masculino para m e feminino para f, caso seja diferente de um dos dois, diga indefinido
genero = input("Digite o gênero (M ou F): ").upper()

if genero == "M":
    print(f"{genero} é masculino")
elif genero == "F":
    print(f"{genero} é feminino")
else:
    print(f"{genero} é indefinido")