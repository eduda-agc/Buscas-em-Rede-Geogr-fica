# main.py -> futuramente: interface para selecionar busca, início e fim

from rede_geografica import rede_geografica, plotar_grafo
from rede_geografica.dados import EXEMPLO

def main():
    n = EXEMPLO["n"]
    lambd = EXEMPLO["lambd"]

    G, pos = rede_geografica(n, lambd)
    plotar_grafo(G, pos)

if __name__ == "__main__":
    main()
