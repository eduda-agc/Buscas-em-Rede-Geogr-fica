import networkx as nx
from buscas import bfs

from tests.test_data import test_data


def bfs_test():
    """
    Função de teste da bfs
    """

    for test in test_data:
        # Criando o grafo de teste
        pos = [1, 4, 23, 54, 2, 4]
        G = nx.Graph()
        G.add_nodes_from(test["nodes"])
        G.add_edges_from(test["adj_list"])

        # Definiciondo nó inicial e objetivo
        inicio = test["inicio"]
        objetivo = test["objetivo"]

        # Rodando a BFS
        caminho, tempo = bfs(G, pos, inicio, objetivo, False)

        # Exibindo os resultados
        print(f"Grafo: {test['adj_list']}")
        print(f"Início e fim: {inicio} --> {objetivo}")
        print(f"Caminho encontrado: {caminho}")
        print(f"Tempo transcorrido: {tempo}\n")


if __name__ == "__main__":
    bfs_test()


# Para rodar: python -m tests.bfs_test
