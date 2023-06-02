expressao = input("Informe a expressão: ")
pilha = []

if expressao[0] == ')':
    print("Expressão inválida!")

else:
    for x in expressao:
        if x == '(':
            pilha.append(1)
        
        else:
            if x == ')':
                if len(pilha) == 0:
                    pilha.append(1)
                
                else:
                    pilha.pop()

if len(pilha) == 0:
    print("OK!")

else:
    print("Erro!")
