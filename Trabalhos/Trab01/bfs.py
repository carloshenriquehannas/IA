import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import sys

print("Qual o tipo de custo desejado?\n1-Tempo\n2-Distância\n3-Custo do combustível")
tipoCusto = input()

if tipoCusto == '1':
    df = pd.read_csv('ViagensOrigemDestino - Tempo de viagem (min).csv', index_col=0)
    tipoCusto = "o Tempo"
elif tipoCusto =='2':
    df = pd.read_csv('ViagensOrigemDestino - Distância (km).csv', index_col=0)
    tipoCusto = "a Distância"
elif tipoCusto == '3':
    df = pd.read_csv('ViagensOrigemDestino - Custo combustível (reais).csv', index_col=0)
    tipoCusto = "o preço do Combustível"
else:
    print("\nTipo invalido\n")
    sys.exit()


G = nx.DiGraph()

G.add_nodes_from(df.index)
G.add_nodes_from(df.columns)


for origem in df.index:
    for destino in df.columns:
        peso = df.loc[origem, destino]
        if not pd.isna(peso):
            G.add_edge(origem, destino, weight=peso)

def calcular_custo_total(caminho,grafo):
    custo = 0
    for i in range(len(caminho)-1):
        origem = caminho[i]
        destino = caminho[i+1]
        peso = grafo.get_edge_data(origem,destino)['weight']
        custo += peso
    return custo

num_visitados = 0
solucao = {}

def bfs_caminho(grafo, inicio, destino):

    global num_visitados

    queue = [inicio]
    visitados = {inicio}
    edge_to = {inicio : None}
    num_visitados += 1

    while queue:
        atual = queue.pop(0)

        if (atual == destino):
            return edge_to

        for vizinho in grafo[atual]:
            if vizinho not in visitados:
                queue.append(vizinho)
                visitados.add(vizinho)
                edge_to[vizinho] = atual

    return None

def caminho_final(edge_to, end):
    if edge_to is None:
        return None

    curr = end
    res = []
    while curr is not None:
        res.append(curr)
        curr = edge_to[curr]
    return list(reversed(res))

inicio = input("Digite o nó de início: ")
fim = input("Digite o nó de destino: ")

if not G.has_node(inicio) or not G.has_node(fim):
    print("Nós de entrada incorretos")
    sys.exit()  # Encerra o programa

visitados = set()
caminho_atual = []

edge_to = bfs_caminho(G,inicio,fim)
if(edge_to):
    print("O numero de nós visitados foi:", num_visitados)
    caminho = caminho_final(edge_to, fim)
    print("Caminho final:", caminho)
    custo = calcular_custo_total(caminho, G)
    print(tipoCusto, "total do caminho foi:", custo)
else:
    print("Não há caminho entre os nós de inicio e destino")

