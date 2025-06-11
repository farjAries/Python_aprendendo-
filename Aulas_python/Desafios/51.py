#Desenvolva um programa que leia o primeiro tema e a razao de uma PA.
#No final, mostre os 10 pimeiros termos dessa progressão:

tema = int(input("Primeiro tema: "))
razao = int(input("Razão: "))
valor = tema + razao
for x in range(1,11):
    print(valor, end=" -> ")
    valor += razao
print("Acabou")
    