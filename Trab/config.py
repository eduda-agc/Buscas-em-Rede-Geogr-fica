# config.py 

# configurações gerais do projeto podem ser definidas aqui.
plotar = True  # define se os gráficos devem ser plotados por padrão

def reconstroi_caminho(pais, no) -> list[int]:
    '''Reconstrói o caminho do nó inicial 
        até o nó atual usando o dicionário 
        de pais -> nó_pai: nó_filho'''
    caminho = []
    while no is not None:
        caminho.append(no)
        no = pais.get(no)
    return list(reversed(caminho))