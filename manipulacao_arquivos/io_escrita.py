#!/usr/local/bin/python3

# Lendo o csv e salvando o texto formatado no txt
with open('pessoas.csv') as arquivo:
    with open('pessoas.txt', 'w') as saida:  # abre como escrita
        for registro in arquivo:
            pessoa = registro.strip().split(',')
            print('Nome: {}, Idade: {}'.format(*pessoa), file=saida)
            # printa dentro do arquivo
print('Finalizado.')
