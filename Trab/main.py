# main.py
from rede_geografica.grafo import rede_geografica
from rede_geografica.plot import plotar_grafo
from rede_geografica.dados import criar_dados

from buscas.best_first import best_first
from buscas.a_estr import a_estr
from buscas.bfs import bfs
from buscas.dfs import dfs
from buscas.hill_cl_sem_bkt import hill_cl_sem_bkt

from interface import pegar_dados

from random import randint

def main():

    parametros = pegar_dados()  # interface só abre uma vez
    DADOS = criar_dados(parametros)  # gera os dados com os parâmetros da interface

    n = DADOS["n"]
    lambd = DADOS["lambd"]

    # criar a rede geográfica
    G, pos = rede_geografica(n, lambd)
   
    # extrair parâmetros da interface
    modo = parametros.get("modo", "manual")
    algoritmo = parametros.get("busca", "Best-First")
    exibir = parametros.get("plotar", True)

    # definir nós inicial e final
    if modo == "random":
        inicio = 0
        fim = randint(0, n - 1)
    else:
        inicio = parametros.get("inicio", 0)
        fim = parametros.get("fim", n - 1)

    print(f"Início = {inicio}, Fim = {fim}, Algoritmo = {algoritmo}")
    plotar_grafo(G, pos, inicio, fim)
    

    # executar a busca
    match algoritmo:
        case "DFS":
            resultado = dfs(G, pos, inicio, fim, exibir)
        case "BFS":
            resultado = bfs(G, pos, inicio, fim, exibir)
        case "Best-First":
            resultado = best_first(G, pos, inicio, fim, exibir)
        case "A*":
            resultado = a_estr(G, pos, inicio, fim, exibir)
        case "Hill Climbing":
            resultado = hill_cl_sem_bkt(G, pos, inicio, fim, exibir)
        case _:
            print("Algoritmo desconhecido.")
            return

    # mostrar resultado 
    if not resultado:
        print("Nenhum caminho encontrado.")
    else:
        caminho, tempo = resultado
        if exibir:
            print(f"Caminho encontrado: {caminho}")
        else:
            print(f"Caminho encontrado: {caminho}, tempo = {tempo}")

    


if __name__ == "__main__":
    main()

