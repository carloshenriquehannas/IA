import pandas as pd
import networkx as nx
import sys

def bfs_with_stop(start_node, end_node):
    df = pd.read_csv('ViagensOrigemDestino - Tempo de viagem (min).csv', index_col=0)
            
    # Create a directed graph using NetworkX
    Grafo = nx.Graph()

    # Add nodes from the dataframe to the graph
    Grafo.add_nodes_from(df.index)
    Grafo.add_nodes_from(df.columns)

    # Add edges and weights to the graph
    for origem in df.index:
        for destino in df.columns:
            peso = df.loc[origem, destino]
            # Check if there is a value between the origin and destination points
            if not pd.isna(peso):
                Grafo.add_edge(origem, destino, weight=peso)

    # Function that receives the final path and returns the total cost from origin to destination
    def calcular_custo_total(caminho, grafo):
        custo = 0
        # Simply sum the weight of each edge from origin to destination
        for i in range(len(caminho) - 1):
            origem = caminho[i]
            destino = caminho[i + 1]
            peso = grafo.get_edge_data(origem, destino)['weight']
            custo += peso
        return custo

    visited = set()  # Set to store visited nodes
    visited_count = 0  # Counter for visited nodes
    final_path = []  # List to store the final path

    try:
        path = nx.bfs_tree(Grafo, source=start_node)
        for node in path:
            visited.add(node)  # Add the node to the set of visited nodes
            visited_count += 1  # Increment the visited count
            final_path.append(node)  # Add the node to the final path
            if node == end_node:
                break  # Stop the search when the destination node is reached

        #custo = calcular_custo_total(final_path, Grafo)
        custo =0
    
        return final_path, custo, visited_count

    except nx.NetworkXNoPath:
        print("Não foi possível encontrar um caminho entre os nós especificados.")
