expressao = input("Digite a expressão: ")
cont = 0

if ')' == expressao[0]:
  print("Expressão não aceita!")

else:
    for x in expressao:
        if x == '(':
            cont = cont + 1

    for x in expressao:
        if x == ')':
            cont -= 1

    if(cont == 0):
        print("OK!")

    else:
        print("Erro!")