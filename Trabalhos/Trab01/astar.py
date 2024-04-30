import pandas as pd
import networkx as nx
import sys 
import heapq

class node:
    def __init__(self, cidade, antecessor=none, g=0, h=0):
        self.cidade = cidade
        self.antecessor = antecessor 
        self.g = g  # custo do caminho do no inicial ate este no
        self.h = h  # estimativa do custo do caminho deste no ate o objetivo

    def __lt__(self, other):
        return (self.g + self.h) < (other.g + other.h)



def astar(tipocusto, inicio, fim):
    if tipocusto == '1':
        df = pd.read_csv('viagensorigemdestino - tempo de viagem (min).csv', index_col = 0)
        tipocusto = "o tempo"
    elif tipocusto == '2':
        df = pd.read_csv('viagensorigemdestino - distância (km).csv', index_col = 0)
        tipocusto == "a distância"
    elif tipocusto == '3':
        df = pd.read_csv('viagensorigemdestino - custo combustível (reais).csv', index_col = 0)
        tipocusto = "o preço do combustível"
    else:
        # tipo fornecido invalido, erro
        # print("\ntipo invalido\n")
        sys.exit()

    # usa-se a biblioteca networkx para criar o grafo direcionado
    grafo = nx.graph()

    # adiciona-se os nos do dataframe ao grafo
    grafo.add_nodes_from(df.index)
    grafo.add_nodes_from(df.columns)

    # adiciona-se as arestas e os pesos ao grafo
    for origem in df.index:
        for destino in df.columns:
            peso = df.loc[origem,destino]
            # verifica-se se existe um valor entre os pontos de origem e destino
            if not pd.isna(peso):
                grafo.add_edge(origem,destino,weight = peso)

    # verifica a entrada do usuario
    if not grafo.has_node(inicio) or not grafo.has_node(fim):
        # print("\nnós de entrada invalidos\n")
        sys.exit()

    # le as distancias de manhattan entre as cidades e o objetivo e registra elas em um vetor
    def lerheuristica(caminhoheuristica, fim, tipocusto):
        heur = {}
        df2 = pd.read_csv('viagensorigemdestino.csv', index_col = 0)
        for cidade in df2.index:
            heur[cidade] = df2.loc[cidade, fim]
        heur[fim] = 0
        
        # ajustando os valores para o tipo de analise
        if( tipocusto == '1'):
            for h in heur:
                h = h / 100
        elif( tipocusto == '3'):
            for h in heur:
                h = h * 3

        return heur


    #algoritmo busca a*
    def busca_astar(grafo, inicio, fim, heuristica):
        nosvisitados = 0
        
        # cria uma fila de prioridade     
        nosabertos = []
        nosfechados = set()

        noinicial = node(inicio,none, g=0, h=heuristica[inicio])
        heapq.heappush(nosabertos,noinicial)

        # corpo do algoritmo
        while nosabertos:
            # pega o elemento com menor valor de distancia
            noatual = heapq.heappop(nosabertos)
            #print("\n atual: ", noatual.cidade, "\n custo: ", noatual.g, "\nheuristica: ", noatual.h, "\n") 

            # remove outras possibilidades de caminhos para um mesmo no que esta sendo aberto
            for no in nosabertos:
                if no.cidade == noatual.cidade:
                    nosabertos.remove(no)
            heapq.heapify(nosabertos)

            # garante que o no nao foi visitado
            if noatual.cidade in nosfechados:
                continue

            nosvisitados += 1

            #condicao de parada
            if (noatual.cidade == fim):
                #retorna os antecessores e o numero de nos visitados
                caminho = []
                custo = noatual.g
                while noatual:
                    caminho.insert(0,noatual.cidade)
                    noatual = noatual.antecessor
                return caminho, nosvisitados, custo  
        
            nosfechados.add(noatual.cidade)


            # avalia os nos vizinhos e os insere na lista
            for vizinho in grafo[noatual.cidade]:
                # confere se o no ja foi visitado (a* so abre um no se ja se encontrou o melhor caminho para ele)
                if vizinho in nosfechados:   
                    #print("\n no ja fechado\n")
                    continue

                g = noatual.g + grafo.get_edge_data(vizinho, noatual.cidade)['weight'] 
                h = heuristica[vizinho]
                novono = node(vizinho, noatual, g, h)

                # checa se ja existe um caminho melhor para esse no
                for no in nosabertos:
                    if no.cidade == vizinho and (no.g + no.h) <= (g + h):
                        break
                else:
                    #caso cotrario, insere o novo no                    
                    heapq.heappush(nosabertos, novono)
                    #print("\n novo no: ", novono.cidade, "\n custo: ", novono.g, "\nheuristica: ", novono.h, "\n") 

        return none, nosvisitados, none # nao achou caminho
    
    caminhoheuristica = 'viagensorigemdestino.xlsx'
    heuristica = lerheuristica(caminhoheuristica, fim, tipocusto)

    caminho, nosvisitados, custo = busca_astar(grafo, inicio, fim, heuristica)

    return caminho, custo, nosvisitados  



