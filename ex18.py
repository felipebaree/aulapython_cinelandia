#Uma loja de produtos tecnologicos te contratou para desenvolver um codigo da seguite forma:
#Leia um produto e de acordo com o produto verifique o preço. (Vide tabela abaixo)
#produtos-preço
#mouse-10
#teclado-20
#memória-100
#Leia a ainda a quantidade de produtos comprados:
#Calcule:
#total = preco * quantidade
#imposto = se a quantidade for maior que 10 calcule um imposto de
#5% sobre o produto senaō calcule 10%
#valor final = total + imposto
produto = input("Digite o nome do produto (mouse, teclado ou memória): ").lower()
if produto == "mouse":
    preco = 10
elif produto == "teclado":
    preco = 20
elif produto == "memória" or produto == "memoria":
    preco = 100
else:
    print("Produto inválido!")
    exit()

quantidade = int(input("Digite a quantidade comprada: "))

total = preco * quantidade

if quantidade > 10:
    imposto = total * 0.05
else:
    imposto = total * 0.10

valor_final = total + imposto

print(f"Produto: {produto}")
print(f"Preço unitário: R$ {preco}")
print(f"Quantidade: {quantidade}")
print(f"Total: R$ {total}")
print(f"Imposto: R$ {imposto}")
print(f"Valor final a pagar: R$ {valor_final}")

