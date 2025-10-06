numero = int(input("Digite um número inteiro de 3 digitos: "))
print(f"Centena: {numero//100}"),
print(f"Dezena: {(numero//10)%10}")
print(f"Unidade: {numero%10}")