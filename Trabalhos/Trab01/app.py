import streamlit as st
import pandas as pd
from bfs_v2 import buscaBFS

custos = {
    'Tempo': '1',
    'Distância': '2',
    'Custo do combustível': '3'
}

unidade = {
    'Tempo': 'min',
    'Distância': 'km',
    'Custo do combustível': 'Reais'
}

def search(tipo_busca_input, tipo_custo_input, no_inicial, no_final):
    if tipo_busca_input == 'BFS - Busca em Largura':
        caminho, custo, num_visitados = buscaBFS(custos[tipo_custo_input], no_inicial, no_final)
        return {"caminho": caminho, "custo": custo, "visitados": num_visitados}

st.title("Otimizador de Rotas da Pássaro Marron")


tipos_busca = ['BFS - Busca em Largura', 'A*']
tipos_custo = ['Tempo', 'Distância', 'Custo do combustível']

df = pd.read_csv('graph.csv', index_col=0)
cidades = list(df.index)


with st.form("FormBusca"):
    tipo_busca_input = st.radio("Qual tipo de busca deseja usar?", tipos_busca)
    tipo_custo_input = st.selectbox("Qual tipo de custo você deseja otimizar?", tipos_custo)

    no_inicial = st.selectbox("Origem:", cidades)
    no_final = st.selectbox("Destino", cidades)

    botao = st.form_submit_button("Buscar")

if botao:
    resultados = search(tipo_busca_input, tipo_custo_input, no_inicial, no_final)
    with st.container():
        st.header("Resultados:")
        st.write(f"Caminho final: {resultados['caminho']}")
        st.write(f"Custo: {resultados['custo']} {unidade[tipo_custo_input]}")
        st.write(f"Número de nós visitados: {resultados['visitados']}")


