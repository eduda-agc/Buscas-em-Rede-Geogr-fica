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

        # ------------------------------
        # Tipo de Grafo
        # ------------------------------
        tk.Label(frame, text="Tipo de Grafo:", font=("Arial", 12)).grid(row=0, column=0, sticky="w")

        self.modo_var = tk.StringVar(value="manual")
        ttk.Radiobutton(frame, text="Manual", variable=self.modo_var, value="manual",
                        command=self._toggle_manual).grid(row=1, column=0, sticky="w")
        ttk.Radiobutton(frame, text="Aleatório", variable=self.modo_var, value="random",
                        command=self._toggle_manual).grid(row=2, column=0, sticky="w")

        # ------------------------------
        # Quantidade de nós
        # ------------------------------
        tk.Label(frame, text="Quantidade de nós:").grid(row=3, column=0, sticky="w", pady=(10, 0))
        self.entry_n = ttk.Entry(frame, width=10)
        self.entry_n.insert(0, "10")
        self.entry_n.grid(row=4, column=0, sticky="w")

        # ------------------------------
        # Nós inicial e final
        # ------------------------------
        tk.Label(frame, text="Nó inicial:").grid(row=5, column=0, sticky="w", pady=(10, 0))
        self.entry_inicio = ttk.Entry(frame, width=10)
        self.entry_inicio.insert(0, "0")
        self.entry_inicio.grid(row=6, column=0, sticky="w")

        tk.Label(frame, text="Nó final:").grid(row=7, column=0, sticky="w", pady=(10, 0))
        self.entry_fim = ttk.Entry(frame, width=10)
        self.entry_fim.insert(0, "9")
        self.entry_fim.grid(row=8, column=0, sticky="w")

        # ------------------------------
        # Algoritmo
        # ------------------------------
        tk.Label(frame, text="Algoritmo de busca:", font=("Arial", 12)).grid(row=9, column=0, sticky="w", pady=(15, 0))

        self.busca_var = tk.StringVar(value="Best-First")
        self.combo_busca = ttk.Combobox(frame, textvariable=self.busca_var,
            values=["DFS", "BFS", "Best-First", "A*", "Hill Climbing"],
            state="readonly", width=15)
        self.combo_busca.grid(row=10, column=0, sticky="w", pady=5)

        # ------------------------------
        # Exibir animação (CHECKBOX)
        # ------------------------------
        self.plotar_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(frame, text="Exibir animação da busca", variable=self.plotar_var).grid(row=11, column=0, pady=10, sticky="w")

        # ------------------------------
        # Start button
        # ------------------------------
        botao = ttk.Button(self.root, text="Start", command=self._start)
        botao.pack(pady=20)

        self._toggle_manual()
        self.root.bind("<Return>", lambda event: self._start())
        self.root.mainloop()

    def _toggle_manual(self):
        estado = tk.NORMAL if self.modo_var.get() == "manual" else tk.DISABLED
        self.entry_inicio.config(state=estado)
        self.entry_fim.config(state=estado)

    def _start(self):
        try:
            n = int(self.entry_n.get())
            if n < 2: raise ValueError

            modo = self.modo_var.get()

            if modo == "manual":
                inicio = int(self.entry_inicio.get())
                fim = int(self.entry_fim.get())
                if not (0 <= inicio < n and 0 <= fim < n):
                    raise ValueError
            else:
                inicio = None
                fim = None

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

def interface():
    janela = JanelaBusca()
    return janela.parametros

params = None # ppara poder usar em outros lugares sem precisar abrir a interface várias vezes

def pegar_dados():
    global params
    # abre o interface() só uma vez
    if params is None: 
        # Aqui você define ou lê os parâmetros
        params = {"plotar": True, "modo": "manual", "n": 10}
        params = interface()   
    return params



