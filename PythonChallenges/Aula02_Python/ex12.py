contador = 0
while True:
    digitado = int(input("Digite um número positivo: "))
    if digitado < 0:
        break
    contador +=1
print(f"Você digitou {contador} items até digitar um negativo.")