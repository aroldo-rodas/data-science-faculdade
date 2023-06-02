string1 = input("Informe uma string:")
string2 = input("Informe a segunda string: ")
cont = 0

if string2 not in string1:
    print(f"{string2} não está presente em {string1}.")

else:
    print(f"{string2} está presente na posição {string1.find(string2)}")