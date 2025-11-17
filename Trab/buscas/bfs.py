from collections import deque
from time import perf_counter

import networkx as nx
from config import reconstroi_caminho
from rede_geografica.plot import finalizar_plot, plotar_grafo_busca


def bfs(G, pos, inicio, objetivo, exibir):
    """
    Calcula uma busca em largura pelo grafo
    argumentos:
        G - Grafo
        pos - lista de posições de cada nó na rede geográfica
        inicio - Nó inicial
        objetivo - Nó objetivo

    Novo retorno:
        caminho (aparentemente reconstruido...)
        tempo pde execução ou None
        Para o experimento I ainda é preciso retornar a distancia

    Retorno:
        caminho: Lista do caminho percorrido (se der ruim, use a funcao)
        dist: Distância total do caminho (em número de nós?)
        sucesso: booleano para informar se o nó objetivo foi atingido
    """

    # Medindo o tempo de execução
    tempo_exec = perf_counter()

    # Declarando as variáveis auxiliares
    pais = {}  # Usado para reconstruir o caminho
    visitados = set()
    proximos = deque()
    passo = 0

    # inicializando a busca com o no atual
    proximos.append(inicio)
    pais[inicio] = None

    while proximos:
        no_atual = proximos.popleft()

        # Plotando o estado atual da busca na interface
        if exibir:
            plotar_grafo_busca(
                G,
                pos,
                busca="BFS",
                passo=passo,
                visitados=visitados,
                frontera=list(proximos),
                atual=no_atual,
                caminho=reconstroi_caminho(pais, no_atual),
                inc=inicio,
                obj=objetivo,
            )

        # Atualizando os dados com a visita atual
        visitados.add(no_atual)
        passo += 1

        # Verificando se é o objetivo
        if no_atual == objetivo:
            if exibir:
                finalizar_plot()
                return reconstroi_caminho(pais, no_atual), None

            # Retorno com tempo de execução caso não haja interface
            tempo_exec = perf_counter() - tempo_exec
            return reconstroi_caminho(pais, no_atual), tempo_exec

        # Adcionando filhos não-visitados na lista de próximos
        filhos = list(G.adj[no_atual])
        for filho in filhos:
            if filho not in proximos and filho not in visitados:
                proximos.append(filho)
                pais[filho] = no_atual

    return None, None
