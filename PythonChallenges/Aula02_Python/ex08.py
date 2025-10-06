LISTA_GERADA = [2, 4, 6, 8, 9 , 10, 12]
impar = 0
posicao = 0
for item in LISTA_GERADA:
    if item % 2 != 0:
        impar +=1
        break
    posicao +=1
if impar <= 0:
    print("Nenhum ímpar encontrado")
else:
    print(f"Foi encontrado o número impar {LISTA_GERADA[posicao]}")