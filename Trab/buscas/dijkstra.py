import heapq
from time import perf_counter

from config import reconstroi_caminho
from rede_geografica.grafo import dist_euclidiana as distancia
from rede_geografica.plot import finalizar_plot, plotar_grafo_busca


def dijkstra(G, pos, inicio, objetivo, exibir):
    """
    Calcula o caminho de menor custo usando o algoritmo de Dijkstra.

    Este algoritmo encontra o caminho mais curto entre nós em um grafo, 
    que é o que A* faz, mas sem usar uma heurística para guiar a busca.
    A prioridade de um nó na fronteira é simplesmente a distância acumulada 
    desde o nó inicial (custo g(n)).
    """
    tempo_exec = perf_counter()

    # distancias armazena o custo do caminho mais barato conhecido do início até cada nó.
    distancias = {node: float('inf') for node in G.nodes()}
    distancias[inicio] = 0

    # A fronteira é uma fila de prioridade (min-heap) contendo (distancia, nó).
    frontera = [(0.0, inicio)]
    
    # Dicionário para reconstruir o caminho.
    pais = {inicio: None}

    # Conjunto para rastrear nós que já foram expandidos.
    visitados = set()
    passo = 0

    while frontera:
        # Pega o nó na fronteira com a menor distância.
        dist_atual, atual = heapq.heappop(frontera)

        # Se já encontramos um caminho mais curto para este nó, pulamos.
        if dist_atual > distancias[atual]:
            continue

        # Se já expandimos este nó, pulamos para o próximo.
        if atual in visitados:
            continue
        visitados.add(atual)

        # Plotar o estado atual da busca, se a exibição estiver ativa.
        if exibir:
            plotar_grafo_busca(
                G, pos,
                busca="Dijkstra",
                passo=passo,
                visitados=visitados,
                frontera=[n for _, n in frontera],
                atual=atual,
                caminho=reconstroi_caminho(pais, atual),
                inc=inicio,
                obj=objetivo
            )
        passo += 1

        # Se alcançamos o objetivo, reconstruímos e retornamos o caminho.
        if atual == objetivo:
            if exibir:
                finalizar_plot()
                return reconstroi_caminho(pais, atual), None
            
            tempo_exec = perf_counter() - tempo_exec
            return reconstroi_caminho(pais, atual), tempo_exec

        # Explorar os vizinhos do nó atual.
        for viz in G.neighbors(atual):
            # Calcula o custo para chegar ao vizinho através do nó atual.
            custo_aresta = distancia(pos[atual], pos[viz])
            nova_distancia = distancias[atual] + custo_aresta

            # Se encontramos um caminho mais curto para o vizinho...
            if nova_distancia < distancias.get(viz, float('inf')):
                # ...atualizamos as informações do caminho.
                distancias[viz] = nova_distancia
                pais[viz] = atual
                
                # Adicionamos o vizinho à fronteira com sua nova prioridade.
                heapq.heappush(frontera, (nova_distancia, viz))

    # Se a fronteira esvaziar e não encontrarmos o objetivo, não há caminho.
    return None, None
