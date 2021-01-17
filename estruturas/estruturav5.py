#!/usr/local/bin/python3

# str
palavra = 'paralelepipedo'
for letra in palavra:
    # end padrão é quebra de linha, pode ser mudado
    print(letra, end=' ')

print('')

# lista
aprovados = ['Rafaela', 'Pedro', 'Renan', 'Maria']
for posicao, nome in enumerate(aprovados):
    print(f'{posicao + 1})', nome)

print('')

# tupla
dias_da_semana = ('Segunda', 'Terça', 'Quarta',
                  'Quinta', 'Sexta', 'Sábado', 'Domingo')
for dia in dias_da_semana:
    print('Hoje é ', dia)

# Printar a tupla inteira com * antes
print('Dias da semana', *dias_da_semana)
print('1: {}, 2:{}, 3:{}, 4:{}, 5:{}, 6:{}, 7:{}'.format(*dias_da_semana))

print('')

# adiciona sem respeitar a ordem
# set conjunto
letras = set('muito legal')
for letra in letras:
    print(letra)

print('')

# set conjunto
numeros = {1, 2, 3, 4, 5}
for numero in numeros:
    print(numero)
