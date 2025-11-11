#desenvolva um codigo python usando while que digite um nome e imprima, só para o programa ao digitar sair em maiusculo
nome = ""

while nome != "SAIR":
    nome = input("Digite um nome (ou SAIR para encerrar): ").upper()
    
    if nome == "SAIR":
        break #sai do laço wile
print(f"ola {nome}")