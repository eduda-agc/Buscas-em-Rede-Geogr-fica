# buscas/best_first.py

import heapq 
import matplotlib.pyplot as plt
from rede_geografica.plot import plotar_grafo_busca, finalizar_plot
from rede_geografica.grafo import dist_euclidiana as distancia
from config import reconstroi_caminho


def best_first(G, pos, inicio, objetivo, exibir) -> None | tuple[list[int], float]:
    # cria a heap
    frontera = [] 
    # começamos pelo nó de início = raíz 
    heapq.heappush(frontera, (0, inicio)) 
    # conjunto vazio criado
    visitados = set() 
    # inicio = nó raiz 
    pais = {inicio: None}

    passo = 0

    while frontera:
        # pega só o nó daa heap; heap = (prioridade, nó)
        _, atual = heapq.heappop(frontera)

        # verifica se o nó atual já foi visitado
        if atual in visitados:
            continue
        visitados.add(atual)

        # plotar o estado atual da busca
        # G, pos, busca, passo, visitados, frontera, atual, caminho
        if exibir:
            plotar_grafo_busca(
                G, pos,
                busca="Best-First",
                passo=passo,
                visitados=visitados,
                frontera=[n for _, n in frontera],
                atual=atual,
                caminho=reconstroi_caminho(pais, atual),
                inc = inicio,
                obj = objetivo
            )
        passo += 1

        # verifica se cheguei no objetivo
        if atual == objetivo:
            finalizar_plot()
            return reconstroi_caminho(pais, atual), 0.0

        # procurar nos vizinhos
        for viz in G.neighbors(atual):
            if viz not in visitados:
                # quanto mais perto do objetivo, maior a prioridade
                prioridade = distancia(pos[viz], pos[objetivo])
                heapq.heappush(frontera, (prioridade, viz))
                if viz not in pais:
                    pais[viz] = atual

    return None

