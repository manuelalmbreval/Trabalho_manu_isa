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

def afundados (dicionário_embarcacoes, tabuleiro):
    afundados_totais=0
    
    for tipo in dicionário_embarcacoes:
        z = 0
        
        while z < len(dicionário_embarcacoes[tipo]):
            navio = dicionário_embarcacoes[tipo][z]
            quantidade =0 

            for posicao in navio:
                linha = posicao[0]
                coluna = posicao[1]

                if tabuleiro[linha][coluna] == "X":
                    quantidade += 1

            if quantidade == len(navio):
                afundados_totais += 1

            z += 1

    return afundados_totais
