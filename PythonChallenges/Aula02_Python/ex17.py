soma_total = 0
lista_numeros = []
while True:
    digitado = int(input("Digite um número (para parar digite 0): "))
    if digitado == 0:
        break
    elif digitado % 4 == 0:
        continue
    lista_numeros.append(digitado)
    soma_total +=digitado
print(f"A soma total dos núnmeros {lista_numeros} é {soma_total}")