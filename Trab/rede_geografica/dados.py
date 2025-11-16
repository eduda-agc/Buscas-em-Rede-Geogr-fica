# rede_geografica/dados.py

from random import randint

from random import randint

def criar_dados(parametros):
    """
    Recebe 'parametros' vindos da interface e devolve o dicionário com n e λ.
    """

    plotar = parametros.get("plotar", True)
    modo = parametros.get("modo", "manual")

    if modo == "manual" and plotar:
        # n vem diretamente da interface (garantido >= 100 na interface, mas aqui reforçamos)
        n = int(parametros.get("n", 100))
        if n < 100:
            n = 100

    elif modo == "random" and plotar:
        # gera número aleatório (mínimo 100). Ajuste o limite superior se quiser.
        n = randint(100, 200)
    elif not plotar:   
        n = 2000
    else:
        # fallback de segurança
        n = int(parametros.get("n", 100))
        if n < 100:
            n = 100

    # lambdas possíveis 
    lambd_rede = [13, 14, 15]
    l = randint(0, 2)

    print(f"λ escolhido: {lambd_rede[l]}, n = {n}")

    return {
        "n": n,
        "lambd": lambd_rede[l]
    }

