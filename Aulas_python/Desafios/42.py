n1 = int(input("Qual o valor do primeiro? "))
n2 = int(input("Qual o valor do primeiro? "))
n3 = int(input("Qual o valor do primeiro? "))
if n1 + n2 > n3 and n1 + n3 > n2 and n2 + n3 > n1:
    triangulo = "É UM TRIANGULO"
else:
    triangulo = "NÃO É UM TRIAGULO"



if n1 == n2 == n3:
    resultado = "EQUILATERO"
elif n1 == n2 or n1 == n3 or n2 == n3:
    resultado = "ISÓSCELES"
elif n1 != n2 and n2 != n3:
    resultado = "ESCALENO"


print(f"Os segmentos acima {triangulo} {resultado}")