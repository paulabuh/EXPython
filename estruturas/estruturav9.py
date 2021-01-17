#!/usr/local/bin/python3


# exemplo de como seria um switch
def dia_semana(dia):
    # dicionario
    dias = {1: 'Domingo', 2: 'Segunda', 3: 'Terça',
            4: 'Quarta', 5: 'Quinta', 6: 'Sexta', 7: 'Sábado'}
    return dias.get(dia, 'Inválido')


def fim_de_semana(dia):
    dias = {1: 'Fim de Semana', 2: 'Dia de Semana', 3: 'Dia de Semana',
            4: 'Dia de Semana', 5: 'Dia de Semana', 6: 'Dia de Semana', 7: 'Fim de Semana'}
    return dias.get(dia, 'Inválido')


for x in range(1, 9):
    print(x, '/', dia_semana(x), '/', fim_de_semana(x))
