# interface.py

import tkinter as tk
from tkinter import ttk, messagebox

from rede_geografica import rede_geografica
from rede_geografica.plot import finalizar_plot

from buscas.best_first import best_first
from buscas.a_estr import a_estr
from buscas.bfs import bfs
from buscas.dfs import dfs
from buscas.hill_cl_sem_bkt import hill_cl_sem_bkt
        
class JanelaBusca:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Configurar Busca")
        self.root.geometry("420x470")
        self.root.resizable(False, False)

        self.parametros = None  

        titulo = tk.Label(self.root, text="Configurações da Busca", font=("Arial", 16))
        titulo.pack(pady=10)

        frame = tk.Frame(self.root)
        frame.pack(pady=5, anchor="n")

        frame.columnconfigure(0, weight=1)

        # se vai pesonalizar os nós ou se vai deixar ramdômico
        tk.Label(frame, text="Tipo de Grafo:", font=("Arial", 12)).grid(row=0, column=0, sticky="w")

        self.modo_var = tk.StringVar(value="manual")
        ttk.Radiobutton(frame, text="Manual", variable=self.modo_var, value="manual",
                        command=self._toggle_manual).grid(row=1, column=0, sticky="w")
        ttk.Radiobutton(frame, text="Aleatório", variable=self.modo_var, value="random",
                        command=self._toggle_manual).grid(row=2, column=0, sticky="w")

        # número de nós
        tk.Label(frame, text="Quantidade de nós:").grid(row=3, column=0, sticky="w", pady=(10, 0))
        self.entry_n = ttk.Entry(frame, width=10)
        self.entry_n.insert(0, "100")  # valor padrão sempre visível
        self.entry_n.grid(row=4, column=0, sticky="w")


        #nó inicial e nó objeticvo
        tk.Label(frame, text="Nó inicial:").grid(row=5, column=0, sticky="w", pady=(10, 0))
        self.entry_inicio = ttk.Entry(frame, width=10)
        self.entry_inicio.insert(0, "0")
        self.entry_inicio.grid(row=6, column=0, sticky="w")

        tk.Label(frame, text="Nó final:").grid(row=7, column=0, sticky="w", pady=(10, 0))
        self.entry_fim = ttk.Entry(frame, width=10)
        self.entry_fim.insert(0, "9")
        self.entry_fim.grid(row=8, column=0, sticky="w")

        # algoritmo
        tk.Label(frame, text="Algoritmo de busca:", font=("Arial", 12)).grid(row=9, column=0, sticky="w", pady=(15, 0))

        self.busca_var = tk.StringVar(value="Best-First")
        self.combo_busca = ttk.Combobox(frame, textvariable=self.busca_var,
            values=["DFS", "BFS", "Best-First", "A*", "Hill Climbing"],
            state="readonly", width=15)
        self.combo_busca.grid(row=10, column=0, sticky="w", pady=5)

        #exibe a animação
        self.plotar_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(frame, text="Exibir animação da busca", variable=self.plotar_var).grid(row=11, column=0, pady=10, sticky="w")

        # botão "start"
        botao = ttk.Button(self.root, text="Start", command=self._start)
        botao.pack(pady=20)

        # configura o estado inicial dos campos
        self._toggle_manual()
        self.root.bind("<Return>", lambda event: self._start())
        self.root.mainloop()

    # alterna entre modo manual e aleatório
    def _toggle_manual(self):
        if self.modo_var.get() == "manual":
            # habilita tudo no modo manual
            self.entry_inicio.config(state=tk.NORMAL)
            self.entry_fim.config(state=tk.NORMAL)
            self.entry_n.config(state=tk.NORMAL)
        else:
            # desabilita os três campos no modo aleatório
            self.entry_inicio.config(state=tk.DISABLED)
            self.entry_fim.config(state=tk.DISABLED)
            self.entry_n.config(state=tk.DISABLED)

    # inicia a captura dos dados
    def _start(self):
        try:
            modo = self.modo_var.get()

            if modo == "manual":
                # lê n e força mínimo 100
                n = int(self.entry_n.get() or 100)
                if n < 100:
                    n = 100

                # lê início/fim com defaults caso o usuário deixe em branco
                inicio = int(self.entry_inicio.get() or 0)
                fim = int(self.entry_fim.get() or (n - 1))

                # valida
                if not (0 <= inicio < n and 0 < fim < n and inicio != fim and n >= 100):
                    raise ValueError

            else:  # modo == "random"
                # não depende dos campos da interface, valores automáticos tratados em dados
                n = 100   # mínimo garantido
                inicio = None
                fim = None

            # armazena os parâmetros
            self.parametros = {
                "n": n,
                "inicio": inicio,
                "fim": fim,
                "modo": modo,
                "busca": self.combo_busca.get(),
                "plotar": self.plotar_var.get()
            }

            self.root.destroy()

        except ValueError:
            messagebox.showerror("Erro", "Valores inválidos.")

# função para abrir a interface e pegar os dados
def interface():
    janela = JanelaBusca()
    return janela.parametros

params = None # ppara poder usar em outros lugares sem precisar abrir a interface várias vezes

def pegar_dados():
    global params
    # abre o interface() só uma vez
    if params is None: 
        # define ou lê os parâmetros
        params = {"plotar": True, "modo": "manual", "n": 100, "inicio": 0, "fim": 99, "busca": "Best-First"}
        params = interface()   
    return params



