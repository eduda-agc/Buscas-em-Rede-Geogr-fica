import heapq
from time import perf_counter

from config import reconstroi_caminho
from rede_geografica.grafo import dist_euclidiana as distancia
from rede_geografica.plot import finalizar_plot, plotar_grafo_busca


def a_estr(G, pos, inicio, objetivo, exibir):
    """
    Calcula o caminho de menor custo usando o algoritmo A*.

    A função de custo f(n) é a soma do custo do caminho do início até n (g(n))
    e uma heurística (h(n)) que estima o custo de n até o objetivo.

    g(n): Distância euclidiana acumulada desde o nó inicial.
    h(n): Distância euclidiana em linha reta do nó n até o objetivo.
    """
    tempo_exec = perf_counter()

    # g_score armazena o custo do caminho mais barato conhecido do início até cada nó.
    g_score = {node: float('inf') for node in G.nodes()}
    g_score[inicio] = 0

    # f_score é a nossa estimativa do custo total se passarmos por um nó.
    # f_score = g_score + heurística
    f_score_inicio = distancia(pos[inicio], pos[objetivo])
    
    # A fronteira é uma fila de prioridade (min-heap) contendo (f_score, nó).
    frontera = [(f_score_inicio, inicio)]
    
    # Dicionário para reconstruir o caminho.
    pais = {inicio: None}

    # Conjunto para rastrear nós que já foram expandidos.
    visitados = set()
    passo = 0

    while frontera:
        # Pega o nó na fronteira com o menor f_score.
        _, atual = heapq.heappop(frontera)

        # Adicionamos o nó atual no conjunto de visitados
        visitados.add(atual)

        # Plotar o estado atual da busca, se a exibição estiver ativa.
        if exibir:
            plotar_grafo_busca(
                G, pos,
                busca="A*",
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
            tempo_exec = perf_counter() - tempo_exec
            if exibir:
                finalizar_plot()
                return reconstroi_caminho(pais, atual), None
            return reconstroi_caminho(pais, atual), tempo_exec

        # Explorar os vizinhos do nó atual.
        for viz in G.neighbors(atual):
            if viz not in visitados:
            # Calcula o custo para chegar ao vizinho através do nó atual.
                custo_aresta = distancia(pos[atual], pos[viz])
                tentative_g_score = g_score[atual] + custo_aresta

            # Se encontramos um caminho mais curto para o vizinho...
                if tentative_g_score < g_score.get(viz, float('inf')):
                # ...atualizamos as informações do caminho.
                    pais[viz] = atual
                    g_score[viz] = tentative_g_score
                    heuristica = distancia(pos[viz], pos[objetivo])
                    f_score_viz = tentative_g_score + heuristica

                # Adicionamos o vizinho à fronteira com sua nova prioridade.
                    heapq.heappush(frontera, (f_score_viz, viz))

    # Se a fronteira esvaziar e não encontrarmos o objetivo, não há caminho.
    return None, None

