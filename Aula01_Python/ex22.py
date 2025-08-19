segundosDigitados = int(input("Digite a quantidade de segundos: "))

hora = segundosDigitados // 3600
segundosRestantes = segundosDigitados % 3600
minuto = segundosRestantes // 60
segundo = segundosRestantes % 60
print(f"Horas:{hora} Minutos:{minuto} Segundos:{segundo}")