v1 = int(input("Primerio valor: "))
v2 = int(input("Segundo valor: "))
v3 = int(input("Terceiro valor: "))

Valor_junto = [v1, v2, v3]

valor_min = min(Valor_junto)
valor_max = max(Valor_junto)

print(f"""O menor valor digitado foi {valor_min}
O maior valor digitado foi {valor_max}  """)

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))



#Esse é o Jeito do Curso mas o meu tmb funciona 
# Descobrindo o menor
menor = a # ele ja fala q A é o menor
if b < menor: #mas SE A for maior que B o B passa menor 
    menor = b
if c < menor: #e SE C for menor que B o C passa ser menor 
    menor = c

# Descobrindo o maior
maior = a #A é maior
if b > maior:#mas SE B for maior B se torna o maior
    maior = b
if c > maior:#mas SE C for maior que B se torna maior 
    maior = c

print(f"O menor valor digitado foi {menor}")
print(f"O maior valor digitado foi {maior}")