#!/usr/local/bin/python3
# Shebang - define o interpretador que será usado
import math

if __name__ == '__main__':
    raio = input('Informe o raio: ')
    area = math.pi * (float(raio) ** 2)

print('Área do círculo: ', area)

print('Nome do módulo: ', __name__)
# print('Nome do pacote: ', __package__)
