numero = int(input("Digite um número inteiro: "))
print("*" * numero)
espaco = " " * (numero - 2)
for i in range(numero - 2):
    print("*" + espaco + "*")
if numero > 1:
    print("*" * numero)