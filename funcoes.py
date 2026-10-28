def define_posicoes (linha, coluna, orientacao, tamanho):
    posicoes = []

    for i in range(tamanho):
        if orientacao == "vertical":
            posicoes.append([linha + i, coluna])
        else:
            posicoes.append([linha, coluna+i])

    return posicoes 

def preenche_frota (frota, nome_do_navio, linha, coluna, orientacao, tamanho):
    posicao = define_posicoes(linha, coluna, orientacao, tamanho)
    if nome_do_navio not in frota:
        frota[nome_do_navio]=[]
    frota[nome_do_navio].append(posicao)
    return frota 

def faz_jogada (tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro = 'X'
    else:
        tabuleiro = '-'
    return tabuleiro 




def posiciona_frota(frota):
    tabuleiro = []

    
    for i in range(10):
        linha = []
        for j in range(10):
            linha.append(0)
        tabuleiro.append(linha)

    for tipo in frota:
        
        for navio in frota[tipo]:
            
            for posicao in navio:
                linha = posicao[0]
                coluna = posicao[1]
                tabuleiro[linha][coluna] = 1

    return tabuleiro
    

