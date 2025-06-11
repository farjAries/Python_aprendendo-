kg = float(input("Qual é seu peso? (KG) "))
m = float(input("Qual é sua altura? (m) "))

imc2 = kg / (m ** 2)

if imc2 < 18.5:
    resultado = "MAGREZA"
elif imc2 < 25:
    resultado = "PESO NORMAL"
elif imc2 < 30:
    resultado = "SOBREPESO"
elif imc2 < 40:
    resultado = "OBESIDADE"
else:
    resultado = "OBESIDADE GRAVE"

print(f"O IMC dessa pessoa é de {imc2:.2f}, você está na faixa de {resultado}")
