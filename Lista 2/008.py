string = input("Informe o conjunto de caracteres: ")
dicionario = {}

for x in string:
    dicionario[x] = string.count(x)



print(dicionario)