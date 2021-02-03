#!/usr/local/bin/python3

def soma_3(a, b, c):
    return a + b + c

# gera uma tupla numeros


def soma_n(*numeros):
    soma = 0
    for n in numeros:
        soma += n
    return soma


if __name__ == '__main__':
    print(soma_3(2, 3, 1))
    print(soma_n(2, 2, 2))
    print(soma_n(1, 1, 1, 1, 1, 1))  # packing

    tupla = (1, 2, 3)
    print(soma_3(*tupla))  # unpacking

    lista = [1, 2, 3]
    print(soma_3(*lista))
