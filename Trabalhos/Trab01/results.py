import pandas as pd
from itertools import combinations
from time import time
from bfs_v2 import buscaBFS
from astar import aStar
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('graph.csv', index_col=0)

# 33 cidades -> 528 pares
cidades = df.index.tolist()
duplas_cidades = list(combinations(cidades, 2))

# BFS
nos_visitados_lista = []
tempos_bfs = []

for dupla in duplas_cidades:
    origem, destino = dupla
    inicio = time()
    _, _, num_visitados = buscaBFS('1', origem, destino)
    tempos_bfs.append(time() - inicio)
    nos_visitados_lista.append(num_visitados)

frequencia = {}
for num in nos_visitados_lista:
    frequencia[num] = frequencia.get(num, 0) + 1


# A*
nos_visitados_lista2 = []
tempos_a = []
erros = []

for dupla in duplas_cidades:
    origem, destino = dupla
    inicio = time()
    _, _, num_visitados = aStar('1', origem, destino)        
    tempos_a.append(time() - inicio)
    nos_visitados_lista2.append(num_visitados)

frequencia2 = {}
for num in nos_visitados_lista2:
    frequencia2[num] = frequencia2.get(num, 0) + 1

chaves = sorted(set(frequencia.keys()) | set(frequencia2.keys()))

largura = 0.2  

posicoes = np.arange(len(chaves))

plt.figure(figsize=(10, 6))

barras1 = plt.bar(posicoes - largura / 2, [frequencia.get(chave, 0) for chave in chaves], largura, color='blue', label='BFS')
barras2 = plt.bar(posicoes + largura / 2, [frequencia2.get(chave, 0) for chave in chaves], largura, color='red', label='A*')

plt.xlabel('Número de nós visitados')
plt.ylabel('Frequência')
plt.title('Frequência de nós visitados no BFS e A* - Custo tempo')
plt.xticks(posicoes, chaves)
plt.legend()

plt.show()

media_tempos1 = sum(tempos_bfs) / len(tempos_bfs)
media_tempos2 = sum(tempos_a) / len(tempos_a)

# Imprimir a média dos tempos de execução
print(f'Média dos tempos de execução do BFS: {media_tempos1:.6f} segundos')
print(f'Média dos tempos de execução do A*: {media_tempos2:.6f} segundos')
