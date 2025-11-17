import networkx as nx
from buscas import a_estr, best_first, bfs, dfs, hill_cl_sem_bkt

from tests.dados_teste_busca import dados_teste


def testa_busca(busca):
    """
    Função de teste desacoplada da interface das buscas
    """

    for test in dados_teste:
        # Criando o grafo de teste
        G = nx.Graph()
        G.add_nodes_from(test["nodes"])
        G.add_edges_from(test["adj_list"])

        # Definiciondo nó inicial e objetivo
        inicio = test["inicio"]
        objetivo = test["objetivo"]

        # Rodando a BFS
        caminho, tempo = busca(G, None, inicio, objetivo, False)

        print(f"O que foi retornado: {caminho}")

        # Exibindo os resultados
        if caminho != None:
            print(f"Grafo: {test['adj_list']}")
            print(f"Início e fim: {inicio} --> {objetivo}")
            print(f"Caminho encontrado: {caminho}")
            print(f"Tempo transcorrido: {tempo}\n")
        else:
            print(f"Grafo: {test['adj_list']}")
            print(f"Início e fim: {inicio} --> {objetivo}")
            print("Caminho não encontrado :(")
            print(f"Tempo transcorrido: {tempo}\n")


def configura_teste_da_busca():
    """
    Funçao que permite o usuário escolher qual das buscas utilizar para o teste
    com os dados hardcodados
    """

    buscas = [bfs, dfs, a_estr, hill_cl_sem_bkt, best_first]

    # Esperando o input do usuario
    print("Ecolha a busca:")
    print("0 - bfs")
    print("1 - dfs")
    print("2 - A*")
    print("3 - Hill climb")
    print("4 - best first")

    escolha = int(input())

    # Iniciando o teste
    testa_busca(buscas[escolha])


if __name__ == "__main__":
    configura_teste_da_busca()


# Para rodar: python -m tests.bfs_test
