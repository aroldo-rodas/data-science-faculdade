import os

#Jogo da velha
player1 = input("Informe o nome do Jogador 1: ")
player2 = input("Informe o nome do jogador 2: ")
sair = False
contador = 0

#Matriz do jogo
m = [[7, 8, 9], [4, 5, 6], [1, 2, 3]]

#Limpar o terminal no windows
os.system("cls")

print("Que comecem os jogos!!!\n")
print(f" {m[0][0]} | {m[0][1]} | {m[0][2]}")
print("---+---+---")
print(f" {m[1][0]} | {m[1][1]} | {m[1][2]}")
print("---+---+---")
print(f" {m[2][0]} | {m[2][1]} | {m[2][2]}")

while sair != True:
    print(f"\n{player1} escolha uma posição para jogar: ")
    posicao = int(input())

    if posicao == 1:
        m[2][0] = 'X'

    elif posicao == 2:
        m[2][1] = 'X'

    elif posicao == 3:
        m[2][2] = 'X'
    
    elif posicao == 4:
        m[1][0] = 'X'
    
    elif posicao == 5:
        m[1][1] = 'X'

    elif posicao == 6:
        m[1][2] = 'X'
    
    elif posicao == 7:
        m[0][0] = 'X'

    elif posicao == 8:
        m[0][1] = 'X'

    elif posicao == 9:
        m[0][2] = 'X'

    #Contador
    contador = contador + 1

    #Verifica Empate
    if contador >= 9:
        print("\nEmpate!")
        break


    #Limpar o terminal no windows
    os.system("cls")

    print(f" {m[0][0]} | {m[0][1]} | {m[0][2]}")
    print("---+---+---")
    print(f" {m[1][0]} | {m[1][1]} | {m[1][2]}")
    print("---+---+---")
    print(f" {m[2][0]} | {m[2][1]} | {m[2][2]}")

    if ((m[0][0] == m[0][1]) and (m[0][1] == m[0][2])):
        print(f"O jogador com {m[0][0]} ganhou!")
        sair = True
        break
    
    elif ((m[1][0] == m[1][1]) and (m[1][1] == m[1][2])):
        print(f"O jogador com {m[1][0]} ganhou!")
        sair = True
        break
    
    elif ((m[2][0] == m[2][1]) and (m[2][1] == m[2][2])):
        print(f"O jogador com {m[2][0]} ganhou!")
        sair = True
        break
    
    elif ((m[0][0] == m[1][0]) and (m[1][0] == m[2][0])):
        print(f"O jogador com {m[2][0]} ganhou!")
        sair = True
        break

    elif ((m[0][1] == m[1][1]) and (m[1][1] == m[2][1])):
        print(f"O jogador com {m[0][1]} ganhou!")
        sair = True
        break
    
    elif ((m[0][2] == m[1][2]) and (m[1][2] == m[2][2])):
        print(f"O jogador com {m[0][2]} ganhou!")
        sair = True
        break
    
    elif ((m[2][0] == m[1][1]) and (m[1][1] == m[0][2])):
        print(f"O jogador com {m[2][0]} ganhou!")
        sair = True
        break
    
    elif ((m[0][0] == m[1][1]) and (m[1][1] == m[2][2])):
        print(f"O jogador com {m[1][1]} ganhou!")
        sair = True
        break

    print(f"\n{player2} escolha uma posição para jogar: ")
    posicao = int(input())

    if posicao == 1:
        m[2][0] = 'O'

    elif posicao == 2:
        m[2][1] = 'O'

    elif posicao == 3:
        m[2][2] = 'O'
    
    elif posicao == 4:
        m[1][0] = 'O'
    
    elif posicao == 5:
        m[1][1] = 'O'

    elif posicao == 6:
        m[1][2] = 'O'
    
    elif posicao == 7:
        m[0][0] = 'O'

    elif posicao == 8:
        m[0][1] = 'O'

    elif posicao == 9:
        m[0][2] = 'O'

    #Limpar o terminal no windows
    os.system("cls")

    print(f" {m[0][0]} | {m[0][1]} | {m[0][2]}")
    print("---+---+---")
    print(f" {m[1][0]} | {m[1][1]} | {m[1][2]}")
    print("---+---+---")
    print(f" {m[2][0]} | {m[2][1]} | {m[2][2]}")

    if ((m[0][0] == m[0][1]) and (m[0][1] == m[0][2])):
        print(f"O jogador com {m[0][0]} ganhou!")
        sair = True
        break
    
    elif ((m[1][0] == m[1][1]) and (m[1][1] == m[1][2])):
        print(f"O jogador com {m[1][0]} ganhou!")
        sair = True
        break
    
    elif ((m[2][0] == m[2][1]) and (m[2][1] == m[2][2])):
        print(f"O jogador com {m[2][0]} ganhou!")
        sair = True
        break
    
    elif ((m[0][0] == m[1][0]) and (m[1][0] == m[2][0])):
        print(f"O jogador com {m[2][0]} ganhou!")
        sair = True
        break

    elif ((m[0][1] == m[1][1]) and (m[1][1] == m[2][1])):
        print(f"O jogador com {m[0][1]} ganhou!")
        sair = True
        break
    
    elif ((m[0][2] == m[1][2]) and (m[1][2] == m[2][2])):
        print(f"O jogador com {m[0][2]} ganhou!")
        sair = True
        break
    
    elif ((m[2][0] == m[1][1]) and (m[1][1] == m[0][2])):
        print(f"O jogador com {m[2][0]} ganhou!")
        sair = True
        break
    
    elif ((m[0][0] == m[1][1]) and (m[1][1] == m[2][2])):
        print(f"O jogador com {m[1][1]} ganhou!")
        sair = True
        break
    
    #Contador
    contador = contador + 1
    
    #Verifica Empate
    if contador >= 9:
        print("\nEmpate!")
        break
