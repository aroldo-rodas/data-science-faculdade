lista1 = [1, 2, 3, 4, 5]
lista2 = [1, 2, 8, 7, 6]

lista1 = set(lista1)
lista2 = set(lista2)

lista1.update(lista2)

lista4 = list(lista1)
print(lista4)
