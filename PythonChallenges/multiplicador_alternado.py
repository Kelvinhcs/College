lista_geral = []
numero = int(input("Digite até onde a sequencia vai: "))
for i in range(1, numero+1):
    lista_geral.append(i)
    lista_geral.append(i*2)

print(lista_geral)