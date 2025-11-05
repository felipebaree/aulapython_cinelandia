#desenvolver um codigo python que leia dois nomes se o primeiro for senac ou segundo for cinelandia imprimir SENAC senao imprimir não é senac
nome1=input("digite o primeiro nome")
nome2=input("digite o segundo nome")
if (nome1 == "senac" or nome2 == "cinelandia"):
    print(f"Bem vindo {nome1} {nome2}")
else:
    print(f"voce não é senac")