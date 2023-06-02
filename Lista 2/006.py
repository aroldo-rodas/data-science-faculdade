conjunto1 = {1, 2, 3, 4}
conjunto2 = {1, 1, 5, 6, 4}

#Os valores comuns as duas listas
comum = conjunto1.intersection(conjunto2)
print(f"Os valores comuns as duas listas {comum}!")

#Os valores que só existem na primeira
valor_do_conjunto_1 = conjunto1.difference(conjunto2)
print(f"Os valores que só existem na primeira {valor_do_conjunto_1}!")

#Uma lista com valores não repetidos das duas listas
sem_repeticao = conjunto1.union(conjunto2)
print(f"O conjunto com as duas listas juntas sem repitações configura {sem_repeticao}!")

