velocidade = int(input("Informe o valor da velocidade: "))

if velocidade > 80:
  print("O valor da multa é de R${}.".format(velocidade * 5))
else:
  print("Não houve multa.")
