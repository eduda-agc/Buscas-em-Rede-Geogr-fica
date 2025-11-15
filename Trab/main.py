# main.py
from rede_geografica import rede_geografica, plotar_grafo
from rede_geografica.dados import DADOS_REDE_GEOG as DADOS
from buscas.best_first import best_first
from buscas.a_estr import a_estr
from buscas.bfs import bfs
from buscas.dfs import dfs
from buscas.hill_cl_sem_bkt import hill_cl_sem_bkt

from random import randint

def main():
    n = DADOS["n"]
    lambd = DADOS["lambd"]

    # criar a rede geográfica
    G, pos = rede_geografica(n, lambd)
    plotar_grafo(G, pos, "Rede Geográfica (Inicial)")

    comnd = int(input("Qual busca gostaria de fazer?\n" \
                "Busca em profundidade (1)\n" \
                "Busca em largura (2)\n" \
                "Algoritmo Best-First (3)\n" \
                "Algoritmo A* (4)\n" \
                "Hill Climbing (sem backtracking) (5)\n"))
    busca_escolhida, comnd = resposta(comnd)

    inicio = 0
    objetivo = randint(0, n-1)
    print(f"Rodando {busca_escolhida} de {inicio} para {objetivo}...", flush = True)
    
    caminho, tempo_exec = busca(comnd, G, pos, inicio, objetivo)
    if caminho == None:
        print("Caminho não encontrado")
    else:
        print(f"Caminho encontrado: {caminho} em {tempo_exec:.6f} segundos", flush = True)


def resposta(c) -> str:
    possiveis_buscas = ["Busca em profundidade", "Busca em largura", "Algoritmo Best-First", "Algoritmo A*", "Hill Climbing (sem backtracking)"]
    if ((c != 1) and (c != 2) and (c != 3) and (c != 4) and (c != 5)):
        print("Comando inválido. Tente novamente digitando um número inteiro ccom as respostas correspondentes:")
        print("Busca em profundidade (1)")
        print("Busca em largura (2)")
        print("Algoritmo Best-First (3)")
        print("Algoritmo A* (4)")
        print("Hill Climbing (sem backtracking) (5)")
        exit()
    else:
        s = possiveis_buscas[c]
    return s, c

def busca (c, G, pos, inicio, objetivo) -> None | tuple[list[int], float]:
    match(c):
        case 1:
            return dfs(G, pos, inicio, objetivo)
        case 2:
            return bfs(G, pos, inicio, objetivo)
        case 3:
            return best_first(G, pos, inicio, objetivo)
        case 4:
            return a_estr(G, pos, inicio, objetivo)
        case 5:
            return hill_cl_sem_bkt(G, pos, inicio, objetivo)
        case _: 
            return None, None
    

if __name__ == "__main__":
    main()
