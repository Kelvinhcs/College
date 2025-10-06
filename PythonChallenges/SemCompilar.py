from random import randint
jogadas = 10
vidas = 3
vitorias = 0
opcoes = ['Pedra', 'Papel', 'Tesoura']
while vidas > 0:
    if jogadas < 0:
        break
    else:
        print(f"Você tem {jogadas} jogadas e {vidas} vidas")
        print("""[1] Pedra
[2] Papel
[3] Tesoura""")
        escolha_sistema = randint(0,2)
        while True:
            escolha_usuario = int(input("Qual sua escolha?"))
            if escolha_usuario in (1,2,3):
                break
            else:
                print("Digite novamente o número por favor...")
        if escolha_usuario == escolha_sistema:
            print("Parabéns você acertou!!!!!")
            jogadas -= 1
            vitorias += 1

        else:
            print(f"Que pena, você escolheu {opcoes[escolha_usuario]} e o sistema escolheu {opcoes[escolha_sistema]}")
            vidas -=1
            jogadas -= 1

print(f"Você terminou com {vidas} vidas, {jogadas} jogadas e {vitorias} vitorias")