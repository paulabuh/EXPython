#!/usr/local/bin/python3

def get_dia(dia):
    dias = {
        (1, 7): 'Fim de Semana',
        tuple(range(2, 7)): 'Dia Normal'
    }
    generator = (tipo for numeros, tipo in dias.items() if dia in numeros)
    return next(generator, 'Inválido')


for dia in range(1, 9):
    print(f'{dia}: {get_dia(dia)}')
