saldo = 815.35
saques = 0
while saldo > 50:
    saldo -= 50
    saques +=1
print(f"Foram realizados {saques} saques.")
print(f"Saldo final de R${saldo:.2f}")