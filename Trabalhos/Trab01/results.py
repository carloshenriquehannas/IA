import pandas as pd
from itertools import combinations
from time import time
from bfs_v2 import buscaBFS
from astar import aStar
import matplotlib.pyplot as plt

df = pd.read_csv('graph.csv', index_col=0)

# 33 cidades -> 528 pares
cidades = df.index.tolist()
duplas_cidades = list(combinations(cidades, 2))

nos_visitados_lista = []
tempos = []

for dupla in duplas_cidades:
    origem, destino = dupla
    inicio = time()
    _, _, num_visitados = buscaBFS('1', origem, destino)
    tempos.append(time() - inicio)
    nos_visitados_lista.append(num_visitados)

frequencia = {}
for num in nos_visitados_lista:
    frequencia[num] = frequencia.get(num, 0) + 1

plt.bar(frequencia.keys(), frequencia.values())
plt.xlabel('Número de nós visitados')
plt.ylabel('Frequência')
plt.title('Frequência de nós visitados no BFS')
plt.show()


