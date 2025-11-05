#desenvolva um codigo python que leia um cargo de funcionario, de acordo com o cargo mostre o salario, vide tabela abaixo
#caixa  - 1500
#vendedor-2400
#gerente-4000
#de acordo com os salarios acima, calcule:
#inss=12% sobre salario
#irrf se o salario for maior que 2000 e o irrf sera de 14% sobre o salario, senao sera de 8%
#salario final= salario-irrf-inss
cargo=input("Digite o cargo (Caixa, Vendedor ou Gerente): ").lower()
caixa=1500
vendedor=2400
gerente=4000
if cargo == "caixa":
    salario = 1500
elif cargo == "vendedor":
    salario = 2400
elif cargo == "gerente":
    salario = 4000
else:
    print("Cargo inválido!") 
    exit()   
inss = salario * 0.12
if salario > 2000:
    irrf = salario * 0.14
else:
    irrf = salario * 0.08

salario_final = salario - inss - irrf
print(f"Salário final: R$ {salario_final}")