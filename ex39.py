# 4) Gerador automático de jogos da Mega-Sena

import random  # <-- sem espaço antes!

print("🍀 Gerador de Números da Mega-Sena 🍀")
print("-------------------------------------")

gerar_novo_jogo = 's'

# O loop continua enquanto a resposta for 's' ou 'S'
while gerar_novo_jogo.lower() == 's':
    
    # 1. Geração dos 6 números únicos entre 1 e 60
    # O random.sample garante que os números não se repitam.
    numeros_mega = random.sample(range(1, 61), 6)
    
    # 2. Ordena os números para melhor visualização
    numeros_mega.sort()
    
    print("\nSeu Jogo da Mega-Sena Gerado:")
    print(f">>> {numeros_mega}")
    print("-------------------------------------")

    # 3. Pergunta se deseja gerar um novo jogo
    resposta = input("Deseja gerar um NOVO jogo? (s/n): ").strip()
    
