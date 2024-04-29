import pandas as pd
import networkx as nx
import sys

def bfs_with_stop(start_node, end_node):
    df = pd.read_csv('ViagensOrigemDestino - Tempo de viagem (min).csv', index_col=0)
            
    # Usa a biblioteca networkx para criar um grafo direcionado
    Grafo = nx.Graph()

    # Adiciona os nós do dataframe ao grafo
    Grafo.add_nodes_from(df.index)
    Grafo.add_nodes_from(df.columns)

    # Adiciona as arestas e os pesos ao grafo
    for origem in df.index:
        for destino in df.columns:
            peso = df.loc[origem, destino]
            # Verifica se existe um valor entre os pontos de origem e destino
            if not pd.isna(peso):
                Grafo.add_edge(origem, destino, weight=peso)

    # Função que recebe o caminho final e retorna o custo total da origem ao destino
    def calcular_custo_total(caminho,grafo):
        custo = 0
        # Simplesmente soma o peso de cada aresta da origem ao destino
        for i in range(len(caminho)-1):
            origem = caminho[i]
            destino = caminho[i+1]
            peso = grafo.get_edge_data(origem,destino)['weight']
            custo += peso
        return custo

    visited = set()  # conjunto para armazenar os nós visitados
    visited_count = 0  # contador de nós visitados
    final_path = []  # lista para armazenar o caminho final

    try:
        path = nx.shortest_path(Grafo, start_node, end_node)
        for node in path:
            visited.add(node)  # Adiciona o nó ao conjunto de visitados
            visited_count += 1  # Incrementa o contador de visitados
            final_path.append(node)  # Adiciona o nó ao caminho final
            if node == end_node:
                break  # Parar a busca quando o nó destino for alcançado

        custo = calcular_custo_total(final_path, Grafo)
    
        return final_path, custo, visited_count

    except nx.NetworkXNoPath:
        print("Não foi possível encontrar um caminho do nó inicial ao nó destino.")

