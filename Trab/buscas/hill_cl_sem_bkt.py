
from time import perf_counter

from config import reconstroi_caminho
from rede_geografica.grafo import dist_euclidiana as distancia
from rede_geografica.plot import finalizar_plot, plotar_grafo_busca


def hill_cl_sem_bkt(G, pos, inicio, objetivo, exibir):
    """
    Executa uma busca Hill Climbing sem backtracking.

    A cada passo, o algoritmo move-se para o vizinho mais próximo do objetivo,
    continuando até que o objetivo seja alcançado ou um mínimo local seja
    encontrado (um ponto onde nenhum vizinho está mais perto do objetivo).
    """
    tempo_exec = perf_counter()

    atual = inicio
    pais = {inicio: None}
    passo = 0

    while True:
        # Gera o caminho atual para exibição
        caminho_atual = reconstroi_caminho(pais, atual)

        # Pega os vizinhos do nó atual
        vizinhos = list(G.neighbors(atual))
        if not vizinhos:
            # Se não há vizinhos, não há para onde ir.
            break

        # Encontra o melhor vizinho (o mais próximo do objetivo)
        melhor_vizinho = min(vizinhos, key=lambda v: distancia(pos[v], pos[objetivo]))

        if exibir:
            plotar_grafo_busca(
                G, pos,
                busca="Hill Climbing s/ Bkt",
                passo=passo,
                visitados=set(caminho_atual),
                frontera=[melhor_vizinho],
                atual=atual,
                caminho=caminho_atual,
                inc=inicio,
                obj=objetivo
            )
        passo += 1

        # Verifica se chegamos ao objetivo
        if atual == objetivo:
            if exibir:
                finalizar_plot()
                return caminho_atual, None
            tempo_exec = perf_counter() - tempo_exec
            return caminho_atual, tempo_exec



        # Se o melhor vizinho é melhor que o nó atual, avança
        if distancia(pos[melhor_vizinho], pos[objetivo]) < distancia(pos[atual], pos[objetivo]):
            pais[melhor_vizinho] = atual
            atual = melhor_vizinho

        else:
            # Mínimo local: nenhum vizinho é melhor.
            break

    # Se saiu do loop sem encontrar o objetivo, a busca falhou.
    if exibir:
        finalizar_plot() # Finaliza o plot para mostrar o estado final preso
    return None, None
