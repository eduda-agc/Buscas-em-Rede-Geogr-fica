# rede_geografica/plot.py

import matplotlib.pyplot as plt
import networkx as nx

def plotar_grafo(G, pos, titulo="Rede Geográfica") -> None:
    """Desenha o grafo simples."""
    plt.figure(figsize=(6, 6))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray')
    plt.title(titulo)
    plt.show()


def plotar_grafo_busca(G, pos, busca, passo, visitados, frontera, atual, caminho, inc, obj) -> None:
    """Desenha o grafo durante a busca."""
    # ativar modo interativo global
    plt.ion()

    background = None
    nodes = None

    # manter uma única figura global
    fig, ax = plt.subplots(figsize=(6, 6))

    # força fullscreen 
    manager = plt.get_current_fig_manager()
    manager.full_screen_toggle()

    if background is None:
        background, nodes = iniciar_animacao(G, pos, nodes, background, ax, fig)

    fig.canvas.restore_region(background)

    titulo = f"{busca} > Passo {passo}: Nó Atual {atual}, Início {inc}, Objetivo {obj}"

    # define cores dos nós
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

    # seta as cores dos nós
    nodes.set_color(cores)
    ax.set_title(titulo)

    ax.draw_artist(nodes) # atualiza os nós com as novas cores
    fig.canvas.blit(ax.bbox) # atualiza a área do gráfico
    fig.canvas.flush_events() # processa eventos pendentes
    plt.pause(1.5)  # controla velocidade da animação

def finalizar_plot():
    plt.pause(3)      # controla velocidade na ultima etapa

def iniciar_animacao(G, pos, nd, bg, ax, fig):

    ax.clear() # limpa o eixo para redesenhar
    ax.set_title("Busca") # título inicial

    # desenha grafo base (edges + labels)
    nx.draw_networkx_edges(G, pos, ax=ax, edge_color="gray")
    nx.draw_networkx_labels(G, pos, ax=ax)

    # desenha nodes inicial (cor será alterada depois)
    nd = nx.draw_networkx_nodes(G, pos, node_color="lightblue", ax=ax)

    # captura o fundo para animação
    fig.canvas.draw()
    bg = fig.canvas.copy_from_bbox(ax.bbox)

    return bg, nd

