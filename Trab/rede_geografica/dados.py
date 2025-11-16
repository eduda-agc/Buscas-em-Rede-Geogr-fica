# rede_geografica/dados.py

from random import randint

def criar_dados(parametros):
    """
    Recebe 'parametros' vindos da interface e devolve o dicionário com n e λ.
    """

    plotar = parametros.get("plotar", True)
    modo = parametros.get("modo", "manual")

    if modo == "manual":
        # n vem diretamente da interface
        n = parametros["n"]

    elif modo == "random":
        # gera número aleatório
        n = randint(100, 150)

    else:
        # fallback de segurança
        n = parametros.get("n", 10)

    # lambdas possíveis 
    lambd_rede = [4, 5, 6]
    l = randint(0, 2)

    print(f"λ escolhido: {lambd_rede[l]}, n = {n}")

    return {
        "n": n,
        "lambd": lambd_rede[l]
    }
