import pandas as pd
import networkx as nx
import sys

# Solicita ao usuário escolher um tipo de custo
# print("Qual o tipo de custo desejado?\n1-Tempo\n2-Distância\n3-Custo do combustível")
# tipoCusto = input()

def buscaBFS(tipoCusto, inicio, fim):
    # Com base no tipo escolhido abre o csv correspondente
    if tipoCusto == '1':
        df = pd.read_csv('ViagensOrigemDestino - Tempo de viagem (min).csv', index_col=0)
        tipoCusto = "O Tempo"
    elif tipoCusto =='2':
        df = pd.read_csv('ViagensOrigemDestino - Distância (km).csv', index_col=0)
        tipoCusto = "A Distância"
    elif tipoCusto == '3':
        df = pd.read_csv('ViagensOrigemDestino - Custo combustível (reais).csv', index_col=0)
        tipoCusto = "O preço do Combustível"
    else:
        # Caso o tipo fornecido seja incorreto, encerra o programa
        print("\nTipo invalido\n")
        sys.exit()


    # Usa a biblioteca networkx para criar um grafo direcionado
    Grafo = nx.DiGraph()

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
        # Simplesmete soma o peso de cada aresta da origem ao destino
        for i in range(len(caminho)-1):
            origem = caminho[i]
            destino = caminho[i+1]
            peso = grafo.get_edge_data(origem,destino)['weight']
            custo += peso
        return custo

    # Numero total de nós visitados
    num_visitados = 0

    # Função para fazer a busca em largura
    def bfs_caminho(grafo, inicio, destino):
        num_visitados = 0
        # Adiciona o nó inicial a fila e ao conjunto de visitados
        queue = [inicio]
        visitados = {inicio}
        # Declara um dicionário para armazenar o nó anterior do nó visitado
        antecessores = {inicio : None}

        # Percorre a fila
        while queue:
            atual = queue.pop(0)

            # condição de parada se chegar ao destino
            if (atual == destino):
                # retorna o dicionário com os nós anteriores para achar o caminho final
                return antecessores

            # Explora os vizinhos do nó atual 
            for vizinho in grafo[atual]:
                # Confere se o nó já não foi visitado
                if vizinho not in visitados:
                    queue.append(vizinho) # Adiciona o vizinho à fila
                    visitados.add(vizinho) # Marca o vizinho como visitado
                    antecessores[vizinho] = atual # Vincula o antecessor
                    num_visitados += 1 # incrementa o número de nós visitados

        # Caso não encontre nenhum caminho
        return None

    # Função para encontrar o caminho final
    def caminho_final(antecessores, final):
        # Se não houver nenhum antecessores não tem caminho
        if antecessores is None:
            return None

        atual = final
        res = []
        while atual is not None:
            res.append(atual)
            # Vai pegando o nó anterior com base no dicionário
            atual = antecessores[atual]
        return list(reversed(res))

    # Verifica a entrada do usuário
    if not Grafo.has_node(inicio) or not Grafo.has_node(fim):
        print("Nós de entrada incorretos")
        sys.exit()  # Encerra o programa

    # Faz a busca em largura
    antecessores = bfs_caminho(Grafo,inicio,fim)

    # Verifica se a busca foi bem sucedida 
    if(antecessores):
        caminho = caminho_final(antecessores, fim)
        # print("\nO caminho final encontrado foi:", caminho)
        custo = calcular_custo_total(caminho, Grafo)
        # print("\n",tipoCusto, "total do caminho foi:", custo, "\n")
        # print("\nO numero de nós visitados foi:", num_visitados, "\n")
        return caminho, custo, num_visitados 
    else:
        return "\nNão há caminho entre os nós de inicio e destino\n"

