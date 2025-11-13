import random

# --- Variáveis de Controle ---
vitorias_usuario = 0
vitorias_computador = 0
empates = 0

opcoes = ['pedra', 'papel', 'tesoura']

print("--- JOGO: PEDRA, PAPEL, TESOURA ---")
print("O jogo continua até você vencer 3 rodadas!")

while vitorias_usuario < 3:
    print("\n------------------------------")
    print(f"PLACAR ATUAL: Você {vitorias_usuario} x {vitorias_computador} Computador | Empates: {empates}")
    
    escolha_usuario = input("Escolha (Pedra, Papel ou Tesoura): ").strip().lower()
    escolha_computador = random.choice(opcoes)

    if escolha_usuario not in opcoes:
        print("Escolha inválida. Por favor, digite 'pedra', 'papel' ou 'tesoura'.")
        continue

    # 4. Determina o vencedor da rodada (if/elif/else)
    if escolha_usuario == escolha_computador:
        print("Empate!")
        empates += 1
    elif (escolha_usuario == 'pedra' and escolha_computador == 'tesoura') or \
         (escolha_usuario == 'papel' and escolha_computador == 'pedra') or \
         (escolha_usuario == 'tesoura' and escolha_computador == 'papel'):
        print("🎉 VOCÊ VENCEU A RODADA! 🎉")
        vitorias_usuario += 1
    else:
        print("🤖 O computador venceu a rodada.")
        vitorias_computador += 1

# --- Fim do Jogo ---
print("\n==================================")
print(f"FIM DO JOGO! Você alcançou {vitorias_usuario} vitórias.")
print(f"PLACAR FINAL: Você {vitorias_usuario} x {vitorias_computador} Computador (Empates: {empates})")
print("PARABÉNS PELA VITÓRIA!")
print("==================================")
