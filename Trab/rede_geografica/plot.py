# rede_geografica/plot.py

import matplotlib.pyplot as plt
import networkx as nx

import matplotlib.pyplot as plt
import networkx as nx

FIG = None
AX = None
NODES = None
BACKGROUND = None


def plotar_grafo(G, pos, inicio, fim) -> None:
    """Desenha o grafo simples destacando início e fim."""
    
    plt.figure(figsize=(6, 6))

    node_colors = []
    node_sizes = []

    for node in G.nodes():
        if node == inicio:
            node_colors.append("blue")
            node_sizes.append(450)
        elif node == fim:
            node_colors.append("red")
            node_sizes.append(450)
        else:
            node_colors.append("lightgray")
            node_sizes.append(300)

    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color=node_colors,
        node_size=node_sizes,
        edge_color="gray",
        font_size=8,
        font_color="black"
    )

    titulo = f"Rede Geográfica Inicial\nInício: {inicio}   |   Objetivo: {fim}"
    plt.title(titulo)

    plt.show()
    plt.close() 


def plotar_grafo_busca(G, pos, busca, passo, visitados, frontera, atual, caminho, inc, obj):
    global FIG, AX, NODES, BACKGROUND

    plt.ion()

    # cria a figura só na primeira vez
    if FIG is None:
        FIG, AX = plt.subplots(figsize=(6, 6))
        manager = plt.get_current_fig_manager()
        manager.full_screen_toggle()
        BACKGROUND, NODES = iniciar_animacao(G, pos, None, None, AX, FIG)

    FIG.canvas.restore_region(BACKGROUND)

    titulo = f"{busca} > Passo {passo}: Nó Atual {atual}, Início {inc}, Objetivo {obj}"

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

    NODES.set_color(cores)
    AX.set_title(titulo)

    AX.draw_artist(NODES)
    FIG.canvas.blit(AX.bbox)
    FIG.canvas.flush_events()
    plt.pause(1)


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

