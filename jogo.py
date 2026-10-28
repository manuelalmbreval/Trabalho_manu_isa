from funcoes import *

frota={}
nome_do_navio = input("Nome do navio: ")
linha= int(input('linha:  '))
coluna=int(input('coluna:  '))
orientacao= input('orientação:  ')
tamanho=int(input('tamanho:  '))

coordenadas_navio= define_posicoes(linha, coluna, orientacao, tamanho)

print (coordenadas_navio)

frota = preenche_frota (frota, nome_do_navio, linha, coluna, orientacao, tamanho)
print (frota)

