# FOR
# ESTRUTURA DE LAÇO C 

for c in range(6, 0, -1):
    print(c)
print("FIM")
#LEMBRANDO QUE QUANDO QUISER MEXER COM NUMERO NAO ADIANTA colocar zero pq de qualquer forma ele para um antes; ent se pegar o codigo a baixo ele vai começar pelo 0 e terminar com o 5 "MAS SE COLOCAR 1,6" de qualquer forma ele termina com o 5
for n in range(1,6):
    print(n)

s = 0
for c in range(0,3):
    Valor = int(input("QUAL o valor?"))
    s += Valor # Isso é igual a s = s + Valor
print(f"a Soma dos Valores da {s}")


for h in range(0, 21, 2):
    print(h)