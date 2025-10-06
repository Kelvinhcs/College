a = int(input("digite um número: "))
b = int(input("Digite outro número: "))
qtd = 0
resultado = 0
com = a*b
while qtd != b:
    resultado += a
    qtd += 1
print(f"Sem *: {resultado}")
print(f"Com *: {com}")