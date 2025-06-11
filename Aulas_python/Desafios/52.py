# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo
num = int(input("Digite um número: "))

for x in range(1, num + 1):
    if num % x == 0:
        print('\033[34m', end='')
    else:
        print('\33[31m', end='') #Agora
    print(f"{x}", end='')
#agora ver se ele vai ser primo
valor=  num ** 2
if valor > 2 and num // valor:
    print("é Primo ")
else:
    print("Não é primo")