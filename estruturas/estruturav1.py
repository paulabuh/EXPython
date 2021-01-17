#!/usr/local/bin/python3
import sys
import errno


def conceito(nota):
    if nota >= 10:
        return 'Nota Inválida'
    elif nota >= 9.1:
        return 'A'
    elif nota >= 8.1:
        return 'A-'
    elif nota >= 7.1:
        return 'B'
    elif nota >= 6.1:
        return 'B-'
    elif nota >= 5.1:
        return 'C'
    elif nota >= 4.1:
        return 'C-'
    elif nota >= 3.1:
        return 'D'
    elif nota >= 2.1:
        return 'D-'
    elif nota >= 1.1:
        return 'E'
    elif nota >= 0:
        return 'E-'
    else:
        return 'Nota Inválida'


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('ERR: Não informada a nota no parâmetro.')
        sys.exit(errno.EPERM)

    if not sys.argv[1].isnumeric():
        print('ERR: Valor informado não numérico.')
        sys.exit(errno.EINVAL)

    print('Conceito: ', conceito(float(sys.argv[1])))
