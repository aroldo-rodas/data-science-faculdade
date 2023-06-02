frase = input("Informe uma frase ou palavra: ")
dicionario = {}

for x in frase:
    dicionario[x] = frase.count(x)

print(dicionario)

