#!/usr/local/bin/python3

def tag_bloco(conteudo, *args, classe='success', inline=False):
    tag = 'span' if inline else 'div'
    html = conteudo if not callable(conteudo) else conteudo(*args)
    return f'<{tag} class="{classe}">{html}</{tag}>'


def tag_lista(*itens):
    lista = ''.join(f'<li>{item}</li>' for item in itens)
    return f'<ul>{lista}</ul>'


# testes - assertions
assert tag_bloco('Incluindo') == '<div class="success">Incluindo</div>'
# assert tag_bloco(
#     'Incluindo', 'error') == '<div class="success">Incluindo</div>'

print(tag_bloco('Teste'))
print(tag_bloco('Incluindo', inline=True))

print(tag_bloco(tag_lista('Item1', 'Item 2'), classe='info'))

# após passar o parametro *, não pode mais usar parametro posicional,
# tem que passar o nome. Exemplo de Callable no primeiro parametro
# Exemplo de packing no segundo parametro
print(tag_bloco(tag_lista, 'Item1', 'Item 2', classe='info', inline=True))
