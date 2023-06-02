n = None
cont = 0
soma = 0
media = 0

while n != 0:
    n = int(input("Informe um número e 0 para sair: "))
    if n != 0:
        cont += 1
        soma += n

if cont > 0:
    media = soma / cont

print("Foram digitados {} números, sua soma é de {} e média de {}.".format(cont, soma, media))