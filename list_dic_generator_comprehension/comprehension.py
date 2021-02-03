#!/usr/local/bin/python3

# [expressao for item in list if condicional]
dobros = [i * 2 for i in range(11)]
print(dobros)

pares = [i * 2 for i in range(11) if i % 2 == 0]
print(pares)

# generator
# consome menos memória pois gera sob demanda ao chamar o next
generator = (i ** 2 for i in range(11) if i % 2 == 0)
print(next(generator))
print(next(generator))
print(next(generator))

generator2 = (i ** 2 for i in range(11) if i % 2 == 0)
for numero in generator2:  # com o for nem precisa chamar o next
    print(numero)

# dicionario
dicionario = {i: i * 2 for i in range(1, 11) if i % 2 == 0}
print(dicionario)

for numero, dobro in dicionario.items():
    print(f'{numero} x 2 = {dobro}')
