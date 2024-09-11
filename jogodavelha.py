import os
import random
from colorama import Fore

# Variáveis
jogarNovamente = "s"
jogadas = 0
quemJoga = 2
maxJogadas = 9
vit = "n"
velha = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

# Função
def tela():
    global velha
    global jogadas
    os.system('cls' if os.name == 'nt' else 'clear')
    print("    0   1   2")
    print("0:  " + velha[0][0] + " | " + velha[0][1] + " | " + velha[0][2])
    print("   -----------")
    print("1:  " + velha[1][0] + " | " + velha[1][1] + " | " + velha[1][2])
    print("   -----------")
    print("2:  " + velha[2][0] + " | " + velha[2][1] + " | " + velha[2][2])
    print("Jogadas: " + Fore.GREEN + str(jogadas) + Fore.RESET)

def jogadorJoga():
    global jogadas
    global quemJoga
    if quemJoga == 2 and jogadas < maxJogadas:
        try:
            l = int(input("Linha..: "))
            c = int(input("Coluna.: "))
            while velha[l][c] != " ":
                l = int(input("Linha..: "))
                c = int(input("Coluna.: "))
            velha[l][c] = "X"
            quemJoga = 1
            jogadas += 1
        except (ValueError, IndexError):
            print("Jogada inválida, tente novamente!")

def cpuJoga():
    global jogadas
    global quemJoga
    if quemJoga == 1 and jogadas < maxJogadas:
        l = random.randrange(0, 3)
        c = random.randrange(0, 3)
        while velha[l][c] != " ":
            l = random.randrange(0, 3)
            c = random.randrange(0, 3)
        velha[l][c] = "O"
        jogadas += 1
        quemJoga = 2

def verificarVitoria():
    global velha
    vitoria = "n"
    simbolos = ["X", "O"]
    for s in simbolos:
        # Verificar vitória em linhas
        for il in range(3):
            if velha[il].count(s) == 3:
                return s
        
        # Verificar colunas
        for ic in range(3):
            if velha[0][ic] == s and velha[1][ic] == s and velha[2][ic] == s:
                return s

        # Verifica diagonal principal
        if velha[0][0] == s and velha[1][1] == s and velha[2][2] == s:
            return s
        
        # Verifica diagonal secundária
        if velha[0][2] == s and velha[1][1] == s and velha[2][0] == s:
            return s

    return vitoria

def redefinir():
    global velha
    global jogadas
    global quemJoga
    global vit
    jogadas = 0
    quemJoga = 2
    vit = "n"
    velha = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]

# Loop principal do jogo
while jogarNovamente == "s":
    while True:
        tela()
        jogadorJoga()
        cpuJoga()
        tela()
        vit = verificarVitoria()
        if vit != "n" or jogadas >= maxJogadas:
            break

    print(Fore.RED + "Fim de jogo" + Fore.YELLOW)
    if vit == "X" or vit == "O":
        print("Resultado: Jogador " + vit + " venceu")
    else:
        print("Resultado: Empate")
    
    jogarNovamente = input(Fore.BLUE + "Jogar Novamente? [s/n]: " + Fore.RESET)
    redefinir()
