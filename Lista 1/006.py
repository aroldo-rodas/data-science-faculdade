instalacao = input("Informe o tipo de instalção: ").upper()
consumo = float(input("Informe o consumo em kWh: "))

if instalacao == 'R':
  if consumo <= 500:
    print("O preço é de R${}.".format(consumo * 0.40))
  else:
    print("O preço é de R${}.".format(consumo * 0.65))
else:
  if instalacao == 'C':
    if consumo <= 1000:
      print("O preço é de R${}.".format(consumo * 0.55))
    else:
      print("O preço é de R${}.".format(consumo * 0.60))
  else:
    if instalacao == 'I':
      if consumo <= 5000:
        print("O preço é de R${}.".format(consumo * 0.55))
      else:
        print("O preço é de R${}.".format(consumo * 0.60))