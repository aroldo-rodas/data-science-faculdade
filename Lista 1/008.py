dividendo = float(input("Informe um número: "))
divisor = float(input("Informe oturo número: "))
cont = 0
resto = 0

#Divisão
while dividendo > 0:
    dividendo = dividendo - divisor
    cont = cont + 1

#Resto da divisão
while cont < 0:
    resto = resto + divisor
    cont = cont - 1 

resto = dividendo - resto

print("A divisão resulta em {} e o resto da visão é {} .".format(cont, abs(resto)))

