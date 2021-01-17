#!/usr/local/bin/python3

# dicionario
produto = {'nome': 'Caneta Chic', 'preco': 14.99,
           'importado': True, 'estoque': 793}

for chave in produto:  # ou produto.keys()
    print(chave)

print('')

for valor in produto.values():
    print(valor)

print('')

for chave, valor in produto.items():
    print(chave, '=', valor)

# os valores ficam disponíveis depois do laço
print(chave, valor)
