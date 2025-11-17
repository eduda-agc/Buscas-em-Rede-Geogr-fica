from collections import deque
from time import perf_counter

import networkx as nx
from rede_geografica.plot import finalizar_plot, plotar_grafo_busca


def test_bfs():
    """
    Função de teste da bfs
    """

    # Criando um grafo de teste
    pos = [1, 4, 23, 54, 2, 4]
    G = nx.Graph()
    G.add_nodes_from([1, 2, 3, 4, 5])
    G.add_edges_from([(1, 2), (1, 3), (2, 4), (4, 2)])

    # Definiciondo nó inicial e objetivo
    inicio = 1
    objetivo = 5

    # Rodando a BFS
    caminho, _ = bfs(G, pos, inicio, objetivo, False)

    # Exibindo os resultados
    print(f"Caminho encontrado: {caminho}")


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

    # Declarando as variáveis de retorno
    caminho = []

    # Declarando as variáveis auxiliares
    visitados = {}
    proximos = deque()
    passo = 0

    # iniciocializando a busca com o no atual
    proximos.append(inicio)
    visitados[inicio] = True

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
                caminho=caminho,
                inc=inicio,
                obj=objetivo,
            )

        # Atualizando os dados da visita atual
        caminho.append(no_atual)
        passo += 1

        # Verificando se é o objetivo
        if no_atual == objetivo:
            if exibir:
                finalizar_plot()
                return caminho, None

            # Retorno com tempo de execução caso não haja interface
            tempo_exec = perf_counter() - tempo_exec
            return caminho, tempo_exec

        # Adcionando filhos não-visitados na lista de próximos
        filhos = list(G.adj[no_atual])
        for filho in filhos:
            if not visitados.get(filho, False):
                proximos.append(filho)
                visitados[filho] = True  # Impede looops

    return None, None


if __name__ == "__main__":
    test_bfs()
