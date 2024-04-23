
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

df = pd.read_csv('graph.csv', index_col=0)

G = nx.DiGraph()

G.add_nodes_from(df.index)
G.add_nodes_from(df.columns)


for origem in df.index:
    for destino in df.columns:
        peso = df.loc[origem, destino]
        if not pd.isna(peso):
            G.add_edge(origem, destino, weight=peso)

visited = []
queue = []
edge_to = {}


def dfs_caminho(grafo, atual, destino, visitados, caminho):
    visitados.add(atual)
    caminho.append(atual)

    if(atual == destino):
        print("Caminho final:", caminho)
    else:
        for vizinhos in grafo[atual]:
            if vizinhos not in visitados:
                dfs_caminho(grafo, vizinhos, destino, visitados,caminho)
    caminho.pop()

inicio = input("Digite o nó de início: ")
fim = input("Digite o nó de destino: ")

visitados = set()
caminho_atual = []

dfs_caminho(G,inicio,fim,visitados,caminho_atual)
