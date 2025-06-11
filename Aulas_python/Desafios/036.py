#ESCREVA UM PROGRAMA PARA APROVAR O EMRPESTIMO BANCARIO PARA A COMPRA DE UMA CASA. O PROGRAMA VAI PERGUNTAR O VALOR DA CASA, O SALARIO DO COMPRADOR E EM QUANTOS ANOS ELE VAI PAGAR. CALCULE O VALOR DA PRESTAÇAO MENSAL, SABENDO QUE ELA NAO PODE EXCEDER 30% DO SALARIO OU ENTAO O EMPRESTIMO SERA NEGADO

Valor_casa = float(input('Qual o valor da casa: '))
Valor_salario = float(input('Qual seu salario: '))
Valor_anos = int(input('Quantos anos o comprador vai pagar: '))
taxa = 0.02
prestaçao = Valor_casa / (Valor_anos * 12)
total = (Valor_casa * 0.02) / (1 - (1 + taxa) ** - Valor_casa)

if total < 0.30 * Valor_salario:
    print(f'Para pagar uma casa de R${Valor_casa:.2f} em {Valor_anos}anos a prestaçao sera de {prestaçao}, Emprestimo aceito')
else:
    print(f'Para pagar uma casa de R${Valor_casa:.2f} em {Valor_anos:.2f}anos a prestaçao sera de {prestaçao:.2f}, Emprestimo NEGADO')

