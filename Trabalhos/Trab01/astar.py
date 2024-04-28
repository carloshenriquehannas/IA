import pandas as pd
import networkx as nx
import sys 
import heapq

class Node:
    def __init__(self, cidade, antecessor=None, g=0, h=0):
        self.cidade = cidade
        self.antecessor = antecessor 
        self.g = g  # custo do caminho do no inicial ate este no
        self.h = h  # estimativa do custo do caminho deste no ate o objetivo

    def __lt__(self, other):
        return (self.g + self.h) < (other.g + other.h)



def aStar(tipoCusto, inicio, fim):
    if tipoCusto == '1':
        df = pd.read_csv('ViagensOrigemDestino - Tempo de viagem (min).csv', index_col = 0)
        tipoCusto = "O Tempo"
    elif tipoCusto == '2':
        df = pd.read_csv('ViagensOrigemDestino - Distância (km).csv', index_col = 0)
        tipoCusto == "A Distância"
    elif tipoCusto == '3':
        df = pd.read_csv('ViagensOrigemDestino - Custo combustível (reais).csv', index_col = 0)
        tipoCusto = "O preço do Combustível"
    else:
        # Tipo fornecido invalido, erro
        print("\nTipo invalido\n")
        sys.exit()

    # Usa-se a biblioteca networkx para criar o grafo direcionado
    Grafo = nx.Graph()

    # Adiciona-se os nos do dataframe ao grafo
    Grafo.add_nodes_from(df.index)
    Grafo.add_nodes_from(df.columns)

    # Adiciona-se as arestas e os pesos ao grafo
    for origem in df.index:
        for destino in df.columns:
            peso = df.loc[origem,destino]
            # Verifica-se se existe um valor entre os pontos de origem e destino
            if not pd.isna(peso):
                Grafo.add_edge(origem,destino,weight = peso)

    # Verifica a entrada do usuario
    if not Grafo.has_node(inicio) or not Grafo.has_node(fim):
        print("\nNós de entrada invalidos\n")
        sys.exit()

    # Le as distancias de manhattan entre as cidades e o objetivo e registra elas em um vetor
    def lerHeuristica(caminhoHeuristica, fim):
        df2 = pd.read_excel(caminhoHeuristica,sheet_name = "DistânciaReal (km)",index_col = 0) 
        for cidade in df.index:
            heuristica[cidade] = df2.loc[cidade, fim]
        return heuristica

    #Algoritmo busca A*
    def busca_astar(grafo, inicio, fim, heuristica):
        nosVisitados = 0
        
        # Cria uma fila de prioridade     
        nosAbertos[]
        nosFechados = set()

        noInicial = Node(inicio, g=0, h=heuristica[inicio])
        heapq.heappush(nosAbertos,noInicial)

        # Corpo do algoritmo
        while nosAbertos:
            # Pega o elemento com menor valor de distancia
            noAtual = heapq.heappop(nosAbertos)
            nosVisitados += 1

            #condicao de parada
            if (noAtual.cidade == fim):
                #retorna os antecessores e o numero de nos visitados
                caminho = []
                custo = noAtual.g
                while noAtual:
                    caminho.append(noAtual.cidade)
                    noAtual = noAtual.antecessor
                return caminho, nosVisitados, custo  
        
            nosFechados.add(noAtual.cidade)

            # Avalia os nos vizinhos e os insere na lista
            for vizinho in grafo[atual]:
                # Confere se o no ja foi visitado (A* so abre um no se ja se encontrou o melhor caminho para ele)
                if vizinho in nosFechados:   
                    continue

                g = atual.g + grafo.get_edge_data(vizinho, atual.cidade)['weight'] 
                h = heuristica[vizinho]
                novoNo = Node(vizinho, noAtual, g, h)

                # Checa se ja existe um caminho melhor para esse no
                for no in nosAbertos:
                    if no.cidade == vizinho and (no.g + no.h) <= (g + h):
                        break
                else:
                    #Caso cotrario, insere o novo no
                    heapq.heappush(nosAbertos, novoNo)

        return None, nosVisitados # Nao achou caminho
    
    caminhoHeuristica = 'ViagensOrigemDestino.xlsx'
    heuristica = lerHeuristica(caminhoHeuristica, fim)

    caminho, nosVisitados, custo = busca_astar(grafo, inicio, fim, heuristica)

    return caminho, custo, nosVisitados  



