valor = float(input("Preço das compras: R$"))
opcao = int(input("""
FORMAS DE PAGAMENTO
[1] á vista dinheiro/cheque 
[2] á vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartao
QUal é a opção?"""))

if opcao == 1:
    desconto = valor * (10/100)
    resultado = valor - desconto
elif opcao == 2:
    
    desconto = valor * (5/100)
    resultado = valor - desconto
elif opcao == 3:
    resultado = valor

elif opcao == 4:
    parcelas = int(input("Quantas parcelas? "))
    juros = valor * 20 / 100
    resultado = valor + juros
    parcela_valor = resultado / parcelas
    print(f"Sua compra será parcelada em {parcelas}x de R${parcela_valor:.2f} COM JUROS")

print(f"Sua compra de R${valor} vai custar {resultado} no final")
  

