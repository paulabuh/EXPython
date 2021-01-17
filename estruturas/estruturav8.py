#!/usr/local/bin/python3
import random


def sortear_dado():
    return random.randint(1, 6)


for x in range(1, 7):
    if x % 2 != 0:
        continue

    if x == sortear_dado():
        print('Acertou', x)
        break
else:
    print('Não acertou o número')
