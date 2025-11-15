# rede_geografica/plot.py

import matplotlib.pyplot as plt
import networkx as nx

def plotar_grafo(G, pos, titulo="Rede Geográfica") -> None:
    """Desenha o grafo simples."""
    plt.figure(figsize=(6, 6))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray')
    plt.title(titulo)
    plt.show()


def plotar_grafo_busca(G, pos, busca, passo, visitados, frontera, atual, caminho) -> None:
    """Desenha o grafo durante a busca."""

    titulo = f"{busca} — Passo {passo}"

    # Define cores dos nós
    cores = []
    for no in G.nodes():
        if no == atual:
            cores.append("yellow")
        elif no in caminho:
            cores.append("green")
        elif no in visitados:
            cores.append("red")
        elif no in frontera:
            cores.append("orange")
        else:
            cores.append("lightblue")

    # cria a figura
    fig = plt.figure(figsize=(6, 6))

    # pega o manager e coloca fullscreen
    manager = plt.get_current_fig_manager()
    manager.full_screen_toggle()

    # desenha o grafo
    nx.draw(G, pos, with_labels=True, node_color=cores, edge_color='gray', node_size=50)
    plt.title(titulo)

    # exibe sem travar o programa
    plt.show(block=False)

    # espera alguns segundos
    plt.pause(1.5)

    # fecha SOMENTE esta figura
    plt.close(fig)
