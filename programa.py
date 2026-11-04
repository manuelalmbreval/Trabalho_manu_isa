from funcoes import *

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
print (frota)

