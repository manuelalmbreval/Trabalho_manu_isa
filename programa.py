from funcoes import *
import random

frota = {}

navios = {
    "porta-aviões" : [4,1],
    "navio-tanque": [3,2],
    "contratorpedeiro": [2,3],
    "submarino": [1,4]
}

for nome in navios:
    tamanho = navios[nome][0]
    quantidade = navios[nome][1]

    for i in range(quantidade):
        while True:
            print(f"Insira as informações referentes ao navio {nome} que possui tamanho {tamanho}")

            linha = int(input("Linha: "))
            coluna = int(input("Coluna: "))

            if nome == "submarino":
                orientacao = "vertical"
            else: 
                orientacao_numero = int(input("Orientação (1 - vertical / 2 - horizontal): "))

                if orientacao_numero == 1:
                    orientacao = "vertical"
                else:
                    orientacao = "horizontal"

            if posicao_valida (frota, linha, coluna, orientacao, tamanho):
                frota = preenche_frota(frota, nome, linha, coluna, orientacao, tamanho)
                break

            else:
                print("Esta posição não está válida!")

frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}

tabuleiro_oponente = posiciona_frota(frota_oponente)
tabuleiro_jogador = posiciona_frota(frota)

posicoes_informadas = []
posicoes_oponente = []
jogando = True

while jogando:
    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))

    while True:
        linha = int(input("Linha: "))

        while linha < 0 or linha > 9:
            print("Linha inválida!")
            linha = int(input("Linha: "))

        coluna = int(input("Coluna: "))

        while coluna < 0 or coluna > 9:
            print("Coluna inválida!")
            coluna = int(input("Coluna: "))

        if [linha, coluna] in posicoes_informadas:
            print(f"A posição linha {linha} e coluna {coluna} já foi informada anteriormente!")
        else:
            posicoes_informadas.append([linha, coluna])
            break
    tabuleiro_oponente = faz_jogada(tabuleiro_oponente, linha, coluna)

    if afundados(frota_oponente, tabuleiro_oponente) == 10:
        print ("Parabéns! Você derrubou todos os navios do seu oponente!")
        jogando = False


    else:
        while True:
            linha_oponente = random.randint(0, 9)
            coluna_oponente = random.randint(0, 9)

            if [linha_oponente, coluna_oponente] not in posicoes_oponente:
                posicoes_oponente.append([linha_oponente, coluna_oponente])
                break

        print (f"Seu oponente está atacando na linha {linha_oponente} e coluna {coluna_oponente}")

        tabuleiro_jogador = faz_jogada(tabuleiro_jogador, linha_oponente, coluna_oponente)

        if afundados(frota, tabuleiro_jogador) == 10:
            print("Xi! O oponente derrubou toda a sua frota =(")
            jogando = False
            