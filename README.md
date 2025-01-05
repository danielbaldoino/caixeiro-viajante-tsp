# Algoritmo Genético para o Problema do Caixeiro Viajante

Este projeto implementa uma solução para o **Problema do Caixeiro Viajante** (TSP) utilizando um algoritmo genético. O objetivo é encontrar a rota mais curta que passe por todas as cidades, retornando à cidade inicial. A solução é visualizada em um mapa, com a rota plotada ao longo das gerações.

## Requisitos

- Python 3.13
- Bibliotecas:
  - `random`
  - `numpy`
  - `matplotlib`
  - `cartopy`

Você pode instalar as dependências necessárias utilizando o `pip`:

```bash
pip install -r requirements.txt
```

## Estrutura do Código

### Módulos

- **cartopy**: Usado para a visualização do mapa e plotagem das rotas.
- **matplotlib**: Para visualização gráfica.
- **numpy**: Para cálculos de distâncias.
- **random**: Para aleatoriedade nas escolhas do algoritmo genético.

### Parâmetros de Configuração

No início do código, é possível configurar diversos parâmetros que afetam o comportamento do algoritmo e da visualização:

- **Número de cidades** (`num_cidades_plot`): Define quantas cidades serão consideradas no cálculo. O valor deve ser entre 2 e 48.
- **Número de gerações** (`num_geracoes`): Define o número de gerações do algoritmo genético.
- **Cor do mapa** (`mapa_cor`): Define se o mapa será colorido ou não.
- **Zoom do mapa** (`mapa_zoom`): Define se o mapa será exibido com zoom ou não.
- **Parâmetros do algoritmo genético**:
  - **Tamanho da população** (`tamanho_populacao`): Número de indivíduos na população.
  - **Taxa de mutação** (`taxa_mutacao`): Probabilidade de ocorrer uma mutação em um cromossomo.
  
### Funções

- **`calcular_distancia(cidade1, cidade2)`**: Calcula a distância Euclidiana entre duas cidades.
- **`calcular_custo(cromossomo)`**: Calcula o custo total (distância) de uma rota representada por um cromossomo.
- **`gerar_populacao_inicial()`**: Gera a população inicial aleatória de rotas.
- **`selecionar_pais(populacao)`**: Seleciona dois pais para o cruzamento, com base na probabilidade proporcional ao custo.
- **`cruzar(pai1, pai2)`**: Realiza o cruzamento entre dois cromossomos (pais).
- **`mutar(cromossomo)`**: Aplica a mutação em um cromossomo.
- **`plotar_rota(melhor_cromossomo, geracao, ax)`**: Plota a melhor rota da geração atual em um mapa.
- **`algoritmo_genetico()`**: Função principal que executa o algoritmo genético.

### Como Executar

1. Altere o arquivo `cidades.py` para definir as cidades e suas coordenadas (no formato de dicionário `{"cidade_nome": (latitude, longitude)}`).
2. Defina o número de cidades e o número de gerações no início do código.
3. Execute o script:

```bash
python main.py
```

O algoritmo exibirá uma visualização interativa do mapa com as rotas geradas ao longo das gerações. O progresso do melhor custo encontrado será mostrado no console.

### Exemplo de Saída

```
Geração 10: Melhor custo = 245.3
Melhor rota: Cidade A -> Cidade B -> Cidade C -> ...
```
