VOGAIS = ['A', 'E','I', 'O', 'U']
quantidade_vogais = 0
print("-+-"*30)
frase_usuario = str(input("Digite uma frase para a contagem das vogais: ")).upper().strip()
for char in frase_usuario:
    if char in VOGAIS:
        quantidade_vogais +=1
print(f"A frase possui {quantidade_vogais} vogais.")