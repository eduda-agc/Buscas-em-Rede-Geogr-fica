# rede_geografica/plot.py

import matplotlib.pyplot as plt
import networkx as nx

def plotar_grafo(G, pos, titulo="Rede Geográfica"):
    """Desenha o grafo geográfico."""
    plt.figure(figsize=(6, 6))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray')
    plt.title(titulo)
    plt.show()
