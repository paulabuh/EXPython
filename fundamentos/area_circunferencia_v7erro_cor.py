#!/usr/local/bin/python3
# Shebang - define o interpretador que será usado
import math
import sys
import errno


class TerminalColor:
    ERRO = '\033[91m'
    NORMAL = '\033[0m'


def help():
    print(TerminalColor.ERRO, 'Não informado o raio.')
    print(TerminalColor.ERRO, 'Sintaxe: {} <raio>'.format(
        sys.argv[0][2:]), TerminalColor.NORMAL)


def calcular(raio):
    return math.pi * (float(raio) ** 2)


if __name__ == '__main__':
    # receber o raio por parametro pelo console sys.argv[1]
    if len(sys.argv) < 2:
        help()
        # sys.exit(1) saída de erro
        sys.exit(errno.EPERM)

    if not sys.argv[1].isnumeric():
        print(TerminalColor.ERRO, 'O raio deve ser numérico.',
              TerminalColor.NORMAL)
        sys.exit(errno.EINVAL)

    raio = sys.argv[1]
    area = calcular(raio)
    print('Área do círculo: ', area)

"""
Pra chamar a função:

- No terminal, entra na pasta:
./area_circunferencia_v5erro.py 12.5

"""
