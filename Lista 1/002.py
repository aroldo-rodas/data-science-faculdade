dias = int(input("Informe a quantidade de dias: "))
horas = int(input("Informe a quantidade de horas: "))
segundos = int(input("Informe a quantidade de segundos: "))

total = (dias * 24 * 60 * 60) + (horas * 60 * 60) + segundos;

print("{} dias, {} horas e {} segundos equivalem a {} segundos!".format(dias, horas, segundos, total))