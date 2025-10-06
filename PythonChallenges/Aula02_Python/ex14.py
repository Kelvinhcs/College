lista_digitados = []
soma_total = 0
while True:
    digitado = int(input("Digite um número inteiro: "))
    soma_total += digitado
    lista_digitados.append(digitado)
    if soma_total >100:
        break
print(f"A soma total dos núnmeros é {soma_total}")