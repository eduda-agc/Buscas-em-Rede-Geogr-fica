# rede_geografica/grafo.py

import networkx as nx
import numpy as np

def dist_euclidiana(p1, p2) -> float:
    """Calcula a distância euclidiana entre dois pontos."""
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def rede_geografica(n, lambd) -> tuple[nx.Graph, dict[int, tuple[float, float]]]:
    """
    Cria um grafo geográfico com n nós.
    Conecta nós com probabilidade p(d) = exp(-λ * d),
    onde 'dist' é a distância euclidiana entre eles.
    """
    G = nx.Graph()
    G.add_nodes_from(range(n))

    # para cada par de vértices gerar um valor aleatório (entre 0 e 1)
    pos = {i: (np.random.uniform(0, 1), np.random.uniform(0, 1)) for i in range(n)}
    nx.set_node_attributes(G, pos, 'pos')

    for i in range(n):
        for j in range(i + 1, n):
            dist = dist_euclidiana(pos[i], pos[j])
            # cálculo de p na fórmula p(distancia) = exp(-λ * distancia)
            p = np.exp(-lambd *dist)
            # se o valor i: (x, y) for menor do que p, é gerada uma aresta entre o par de vértices i
            aux = np.random.rand()
            if aux < p: 
                G.add_edge(i, j)

    return G, pos
