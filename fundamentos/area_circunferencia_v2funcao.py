#!/usr/local/bin/python3
# Shebang - define o interpretador que será usado
import math


def calcular(raio):
    area = math.pi * (float(raio) ** 2)
    print('Área do círculo: ', area)


"""
Pra chamar a função:

- No terminal, entra na pasta:
python
import area_circunferencia_v2funcao
area_circunferencia_v2funcao.calcular(valor do raio)
.
ou 
.
from area_circunferencia_v2funcao import calcular
calcular(valor do raio)
.
ou
.
- pode colocar um alias
import area_circunferencia_v2funcao as circulo
circulo.calcular(valor do raio)
"""
