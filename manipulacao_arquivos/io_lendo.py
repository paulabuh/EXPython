#!/usr/local/bin/python3

# Executar pelo Terminal

# Exemplo 1
arquivo = open('pessoas.csv')
# carrega todo o arquivo na memória. Não é interessante.
dados = arquivo.read()
arquivo.close()

for registro in dados.splitlines():  # Tira os \n do final das linhas
    print('Nome: {}, Idade: {}'.format(*registro.split(',')))

print('Ex 2')
# Exemplo 2
arquivo = open('pessoas.csv')
for registro in arquivo:  # O python vai lendo aos poucos, streaming, é melhor usar esse
    # strip para tirar os \n
    print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))
arquivo.close()

print('Ex 3')
# Exemplo 3 com try para fechar sempre o arquivo, mesmo qdo der erro
arquivo = open('pessoas.csv')
try:
    for registro in arquivo:
        print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))
except IndexError:
    pass  # bloco vazio, não faz nada
finally:
    arquivo.close()

print('Ex 4')
# Exemplo 4 com With, o arquivo sempre será fechado no final. Pode usar com cenexão também.
with open('pessoas.csv') as arquivo:
    for registro in arquivo:
        print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))
