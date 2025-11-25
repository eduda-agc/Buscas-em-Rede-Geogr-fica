
import time
import random
import numpy as np
from rede_geografica.grafo import rede_geografica, dist_euclidiana
from buscas.a_estr import a_estr
from buscas.best_first import best_first
from buscas.bfs import bfs
from buscas.dfs import dfs
from buscas.dijkstra import dijkstra
from buscas.hill_cl_sem_bkt import hill_cl_sem_bkt

def calcular_distancia_caminho(pos, caminho):
    distancia = 0
    for i in range(len(caminho) - 1):
        distancia += dist_euclidiana(pos[caminho[i]], pos[caminho[i+1]])
    return distancia

def main():
    n = 2000
    lambdas = [13, 14, 15]
    num_runs = 10

    algoritmos = {
        "A*": a_estr,
        "Best-First": best_first,
        "BFS": bfs,
        "DFS": dfs,
        "Dijkstra": dijkstra,
        "Hill Climbing": hill_cl_sem_bkt
    }

    for lambd in lambdas:
        print(f"Gerando rede com n={n} e lambda={lambd}...")
        G, pos = rede_geografica(n, lambd)
        print("Rede gerada.")

        print(f"Gerando {num_runs} pares de vértices fixos para a rede com lambda={lambd}...")
        pares_vertices = set()
        while len(pares_vertices) < num_runs:
            inicio, fim = random.sample(range(n), 2)
            if (inicio, fim) not in pares_vertices and (fim, inicio) not in pares_vertices:
                pares_vertices.add((inicio, fim))
        print("Pares de vértices gerados.")

        for nome_algoritmo, func_algoritmo in algoritmos.items():
            print(f"\nExecutando algoritmo: {nome_algoritmo}")
            distancias = []
            tempos = []
            runs_sucesso = 0

            for inicio, fim in pares_vertices:
                resultado = func_algoritmo(G, pos, inicio, fim, False)

                if resultado:
                    caminho, tempo = resultado
                    if caminho is not None and tempo is not None:
                        distancia = calcular_distancia_caminho(pos, caminho)
                        distancias.append(distancia)
                        tempos.append(tempo)
                        runs_sucesso += 1
                        print(f"  Run {runs_sucesso}/{num_runs} sucesso. (inicio={inicio}, fim={fim})")
                        print(f"  Caminho: {caminho}")

            if runs_sucesso > 0:
                avg_distancia = np.mean(distancias)
                avg_tempo = np.mean(tempos)

                print(f"\nResultados para {nome_algoritmo} com lambda={lambd}:")
                print(f"  Distância média do caminho: {avg_distancia:.4f}")
                print(f"  Tempo médio de execução: {avg_tempo:.6f} segundos")
            else:
                print(f"\nNão foi possível obter caminhos para o algoritmo {nome_algoritmo} com lambda={lambd}")

        print("\n" + "="*50 + "\n")

if __name__ == "__main__":
    main()
