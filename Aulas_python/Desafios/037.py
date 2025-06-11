numero = int(input('Digite um número inteiro: '))

print("Escolha uma das bases para conversão: ")
print("[1] Converter para BINARIO")
print('[2] Converter para OCTAL')
print('[3] Converter para HEXADECIMAL')

base = int(input("Sua Opção: "))

if base == 1:
    binario = bin(numero)[2:]
    print(f"Binario: {binario}")
if base == 2:
    octal = oct(numero)[2:]
    print(f"Octal: {octal}")
if base == 3:
    hexa = hex(numero)
    print(f"hexadecimal: {hexa}")
