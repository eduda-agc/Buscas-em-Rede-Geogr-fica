from queue import Queue
import networkx as nx


def test_bfs():
    """
    Função de teste da bfs
    """

    # Criando um grafo de teste
    G = nx.Graph()
    G.add_nodes_from([1, 2, 3, 4, 5])
    G.add_edges_from([(1, 2), (1, 3), (2, 4), (4, 2)])

    # Definindo nó inicial e objetivo
    inicio = 1
    objetivo = 5

    # Rodando a BFS
    caminho, dist, sucesso = bfs(G, inicio, objetivo)

    # Exibindo os resultados
    print(f"Sucesso da busca: {sucesso}")
    print(f"Caminho encontrado: {caminho}")
    print(f"Distância do caminho: {dist}")


def bfs(G, ini, obj):
    """
    Calcula uma busca em largura pelo grafo
    argumentos:
        G - Grafo
        ini - Nó inicial
        obj - Nó objetivo

    Retorno:
        caminho: Lista do caminho percorrido
        dist: Distância total do caminho (em número de nós?)
        sucesso: booleano para informar se o nó objetivo foi atingido
    """

    # Declarando as variáveis de retorno
    caminho = []
    dist = 0.0

    # Declarando as variáveis auxiliares
    visitados = {}
    proximos = Queue()
    sucesso = False

    # Inicializando a busca com o no atual
    proximos.put(ini)
    visitados[ini] = True

    while not proximos.empty():
        no_atual = proximos.get()

        # Atualizando os dados da visita atual
        caminho.append(no_atual)
        dist += 1

        # Verificando se é o objetivo
        if no_atual == obj:
            sucesso = True
            break

        # Adcionando filhos não-visitados na lista de próximos
        filhos = list(G.adj[no_atual])
        for filho in filhos:
            if not visitados.get(filho, False):
                proximos.put(filho)
                visitados[filho] = True  # Impede looops

    return caminho, dist, sucesso


if __name__ == "__main__":
    test_bfs()
