#!/usr/local/bin/python3

def todos_params(*args, **kwargs):
    print(f'args: {args}')
    print(f'kwargs: {kwargs}')


if __name__ == '__main__':
    # apenas args
    todos_params('a', 'b', 'c')
    # args e kwargs nomeados
    todos_params(1, 2, 3, teste=True, valor=12.99)
    todos_params('Ana', False, [1, 2, 3], tamanho='M', fragil=False)
    # Erro - kwargs antes dos args
    # todos_params(primeiro='João', 'Maria')
    todos_params('Maria', primeiro='João')
