from math import factorial
print("-+-"*30)
digitado = int(input("Digite um número para calcular o fatorial: "))
valor_fatorial = digitado
for item in range(digitado, 1, -1):
    valor_fatorial = valor_fatorial*(item-1)
print(f"Feito no dedo: {valor_fatorial}")
print(f"Usando lib: {factorial(digitado)}")