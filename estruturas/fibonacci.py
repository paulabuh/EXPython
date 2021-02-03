#!/usr/local/bin/python3

# Exemplo de trocando valores com pares
def fibonacci_v1(limite):
    penultimo = 0
    ultimo = 1
    print(penultimo, end=',')
    print(ultimo, end=',')
    while True:
        penultimo, ultimo = ultimo, penultimo + ultimo
        if ultimo >= limite:
            break
        print(ultimo, end=',')


# Exemplo lista e somando os dois últimos itens com sum()
def fibonacci_v2(limite):
    resultado = [0, 1]
    # ultimo elemento [-1]
    while resultado[-1] < limite:
        # ou resultado[-1] + resultado[-2]
        resultado.append(sum(resultado[-2:]))
    return resultado


# Exemplo com quantidade usando for
def fibonacci_v3(quantidade):
    resultado = [0, 1]
    # quando ocntador não é usado
    for _ in range(1, quantidade-1):
        resultado.append(sum(resultado[-2:]))
    return resultado


# Exemplo recursivo com tupla
def fibonacci_v4(quantidade, lista=(0, 1)):
    # condição de parada
    if len(lista) == quantidade:
        return lista

    lista = lista + (sum(lista[-2:]),)
    return fibonacci_v4(quantidade, lista)


# Exemplo recursivo com if operador ternário
def fibonacci_v5(quantidade, lista=(0, 1)):
    return lista if len(lista) == quantidade else fibonacci_v4(quantidade, lista + (sum(lista[-2:]),))


fibonacci_v1(1000)
print()

for numero in fibonacci_v2(1000):
    print(numero, end=',')
print()

print(fibonacci_v3(10))
print(fibonacci_v4(10))
print(fibonacci_v5(10))
