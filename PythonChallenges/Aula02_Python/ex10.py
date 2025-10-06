soma_total = 0
numeros_digitados = []
while True:
    digitado = int(input("Digite um número inteiro: "))
    if digitado == 0:
        break
    soma_total +=digitado
    numeros_digitados.append(digitado)
print(f"Os números digitados foram {numeros_digitados}")
print(f"A soma deles é {soma_total}")