import random

import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D

from cidades import todasCidades

# Número de cidades a serem plotadas e número de gerações
num_cidades_plot = 10  # [2/48]
num_geracoes = 50  # [10/10000]

# Parâmetros do Mapa
mapa_cor = True
mapa_zoom = True

# Parâmetros do Algoritmo Genético
tamanho_populacao = 100
taxa_mutacao = 0.1

# Cidades e suas coordenadas
cidades = dict(random.sample(list(todasCidades.items()), num_cidades_plot))
cidade_inicial = 0  # Índice da cidade inicial

# Número de cidades e lista de nomes e coordenadas
num_cidades = len(cidades)
cidade_nomes = list(cidades.keys())
coordenadas = list(cidades.values())

melhor_geracao = 1

def calcular_distancia(cidade1, cidade2):
    return np.sqrt((cidade1[0] - cidade2[0])**2 + (cidade1[1] - cidade2[1])**2)

def calcular_custo(cromossomo):
    distancia_total = 0
    for i in range(num_cidades - 1):
        distancia_total += calcular_distancia(coordenadas[cromossomo[i]], coordenadas[cromossomo[i + 1]])
    distancia_total += calcular_distancia(coordenadas[cromossomo[-1]], coordenadas[cromossomo[0]])  # Fechar ciclo
    return distancia_total

def gerar_populacao_inicial():
    populacao = []
    for _ in range(tamanho_populacao):
        cromossomo = random.sample(range(num_cidades), num_cidades)
        if cromossomo[0] != cidade_inicial:  # Garantir que a cidade inicial seja sempre a mesma
            cromossomo.remove(cidade_inicial)
            cromossomo.insert(0, cidade_inicial)
        populacao.append(cromossomo)
    return populacao

def selecionar_pais(populacao):
    custos = [calcular_custo(cromossomo) for cromossomo in populacao]
    probabilidade = [1/custo for custo in custos]
    total_probabilidade = sum(probabilidade)
    probabilidade_normalizada = [p/total_probabilidade for p in probabilidade]
    
    pai1 = random.choices(populacao, weights=probabilidade_normalizada, k=1)[0]
    pai2 = random.choices(populacao, weights=probabilidade_normalizada, k=1)[0]
    return pai1, pai2

def cruzar(pai1, pai2):
    ponto_corte = random.randint(1, num_cidades - 1)
    filho1 = pai1[:ponto_corte] + [cidade for cidade in pai2 if cidade not in pai1[:ponto_corte]]
    filho2 = pai2[:ponto_corte] + [cidade for cidade in pai1 if cidade not in pai2[:ponto_corte]]
    return filho1, filho2

def mutar(cromossomo):
    for i in range(1, num_cidades):  # Começa a partir de 1 para não alterar a cidade inicial
        if random.random() < taxa_mutacao:
            j = random.randint(1, num_cidades - 1)  # Troca dois genes (cidades) sem alterar a cidade inicial
            cromossomo[i], cromossomo[j] = cromossomo[j], cromossomo[i]

def plotar_rota(melhor_cromossomo, geracao, ax):
    ax.clear()

    if mapa_zoom == False:
        ax.set_extent([-180, 180, -90, 90], crs=ccrs.PlateCarree())

    if mapa_cor:
        ax.stock_img()
    else:
        ax.add_feature(cfeature.COASTLINE)

    rota = [coordenadas[melhor_cromossomo[i]] for i in range(num_cidades)] + [coordenadas[melhor_cromossomo[0]]]
    latitudes = [p[0] for p in rota]
    longitudes = [p[1] for p in rota]

    # ax.plot(longitudes, latitudes, color='red', marker='o', transform=ccrs.PlateCarree())

    for nome, (lat, lon) in cidades.items():
        cor = 'green' if nome == cidade_nomes[cidade_inicial] else 'blue'
        tamanho = 10 if nome == cidade_nomes[cidade_inicial] else 5

        ax.plot(lon, lat, marker='o', color=cor, markersize=tamanho, label=nome, transform=ccrs.PlateCarree())
        ax.text(lon + 2, lat, nome, transform=ccrs.PlateCarree())

    for i in range(len(longitudes) - 1):
        ax.annotate('', xy=(longitudes[i+1], latitudes[i+1]), xytext=(longitudes[i], latitudes[i]),
                    arrowprops=dict(arrowstyle="->", color='red'), transform=ccrs.PlateCarree())

    legend_elements = [
        Line2D([0], [0], marker='o', color='w', label='Início/Fim', markerfacecolor='green', markersize=10),
        Line2D([0], [0], marker='o', color='w', label='Cidades', markerfacecolor='blue', markersize=7),
        Line2D([0], [0], linestyle='-', color='red', label='Rotas')
    ]

    ax.legend(handles=legend_elements, loc='upper right', bbox_to_anchor=(0.98, 0.98), frameon=True)

    ax.set_title(f"Melhor rota na Geração {geracao}/{num_geracoes} - Partindo de {cidade_nomes[cidade_inicial]}")
    ax.text(0.5, -0.1, f"Tamanho da população: {tamanho_populacao} - Taxa de mutação: {taxa_mutacao}",
            horizontalalignment='center', verticalalignment='center', transform=ax.transAxes)

    plt.pause(0.001)

def algoritmo_genetico():
    populacao = gerar_populacao_inicial()
    melhor_custo_historico = float('inf')
    melhor_cromossomo_historico = None

    _, ax = plt.subplots(figsize=(12, 6), subplot_kw={'projection': ccrs.PlateCarree()})
    
    for geracao in range(1, num_geracoes + 1):
        nova_populacao = []
        while len(nova_populacao) < tamanho_populacao:
            pai1, pai2 = selecionar_pais(populacao)
            filho1, filho2 = cruzar(pai1, pai2)
            mutar(filho1)
            mutar(filho2)
            nova_populacao.extend([filho1, filho2])
        
        populacao = nova_populacao[:tamanho_populacao]

        melhor_cromossomo = min(populacao, key=lambda cromossomo: calcular_custo(cromossomo))
        melhor_custo = calcular_custo(melhor_cromossomo)

        if melhor_custo < melhor_custo_historico:
            melhor_custo_historico = melhor_custo
            melhor_cromossomo_historico = melhor_cromossomo
        
        if geracao % melhor_geracao == 0:
            print(f"Geração {geracao}: Melhor custo = {melhor_custo_historico}")
            print(f"Melhor rota: {' -> '.join([cidade_nomes[cidade] for cidade in melhor_cromossomo_historico])}")
            plotar_rota(melhor_cromossomo_historico, geracao, ax)
 
    plt.tight_layout()
    plt.show()

algoritmo_genetico()
