#codigo python que verifica se um nome é senac
nome = input("Qual seu nome: ")
sobrenome = input("Digite o sobrenome: ")

nome = nome.upper()
sobrenome = sobrenome.upper()

if nome == "SENAC" and sobrenome == "SANTA LUZIA":
    print(f"Seja bem-vindo {nome} {sobrenome}")
else:
    print("não é Senac")