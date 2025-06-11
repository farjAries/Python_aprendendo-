soma_total = 0 
contador_divisiveis = 0

for numero in range(1, 501):
    if (numero % 2 != 0) and (numero % 3 == 0):
        soma_total = soma_total + numero 
        contador_divisiveis = contador_divisiveis + 1

print(f"A soma de todos os {contador_divisiveis} valores solicitados é {soma_total}")