# rede_geografica/dados.py

from random import randint
from config import plotar
"""
Rede Geográfica
a. (n=2000, λ=0,01)
b. (n=2000, λ=0,02)
c. (n=2000, λ=0,03)
"""
if plotar:
    n = randint(5, 20)
else:
    n = 2000

lambd_rede = [4, 5, 6]
l = randint(0, 2)
print(lambd_rede[l], n)

DADOS_REDE_GEOG = {
    "n": 50,
    "lambd": lambd_rede[l]
}