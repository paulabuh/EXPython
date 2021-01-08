#!/usr/local/bin/python3
# Shebang - define o interpretador que será usado
import math
import sys


def calcular(raio):
    return math.pi * (float(raio) ** 2)


if __name__ == '__main__':
    # receber o raio por parametro pelo console sys.argv[1]
    if len(sys.argv) < 2:
        print('Não informado o raio. Sintaxe: {} <raio>'.format(
            sys.argv[0][2:]))
    else:
        raio = sys.argv[1]  # o 0 é o nome do arquivo chamado
        area = calcular(raio)
        print('Área do círculo: ', area)

"""
Pra chamar a função:

- No terminal, entra na pasta:
./area_circunferencia_v3parametro.py 12.5

"""
