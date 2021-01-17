#!/usr/local/bin/python3
from random import randint

numero = -1
numero_secreto = randint(0, 9)

print('Número secreto Sorteado!\nInforme um número (0 a 9).\n')

while numero != numero_secreto:
    numero = int(input('Diga um palpite: '))

print('\n\nNúmero secreto encontrado! Era o {}.\n'.format(numero_secreto))
