# rede_geografica/grafo.py

import networkx as nx
import numpy as np

def dist_euclidiana(x1, y1, x2, y2):
    """Calcula a distância euclidiana entre dois pontos."""
    return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def rede_geografica(n, lambd):
    """
    Cria um grafo geográfico com n nós.
    Conecta nós com probabilidade p(d) = exp(-λ * d),
    onde 'dist' é a distância euclidiana entre eles.
    """
    G = nx.Graph()
    G.add_nodes_from(range(n))

    pos = {i: (np.random.uniform(0, 1), np.random.uniform(0, 1)) for i in range(n)}
    nx.set_node_attributes(G, pos, 'pos')

    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = pos[i]
            x2, y2 = pos[j]
            dist = dist_euclidiana(x1, y1, x2, y2)
            p = np.exp(-lambd * dist)
            if np.random.rand() < p:
                G.add_edge(i, j)

    return G, pos
