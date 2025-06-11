import time
from random import randint

print("""
    [0] PEDRA
    [1] PAPEL
    [2] TESOURA 
    """)
opcao_jogo = ["PEDRA", "PAPEL", "TESOURA"]
escolhido = int(input("Qual é a sua jogada?"))
mesagens = ["JO", "KEN", 'PO!!!']
for mensagem in mesagens:
    print(mensagem)
    time.sleep(0.6)
computador = randint(0,2)
print("-=" * 10)
print(f'O computador escolheu {opcao_jogo[computador]}')
print(f"JOgador escolheu {opcao_jogo[escolhido]}")
print("-=" * 10)


if escolhido ==  0 and computador == 2 or escolhido ==  1 and computador == 0 or escolhido ==  2 and computador == 1 :
    print("Voce ganhou")

elif escolhido == computador:
    print("EMPATE")

else:
    print("Voce Perdeu")


