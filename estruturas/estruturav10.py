#!/usr/local/bin/python3

PALAVRAS = ('Religião', 'Futebol', 'Política')
textos = ['João gosta de futebol e política.',
          'A praia foi divertida.', 'Ele segue a religião a risca.',
          'Maria gosta de futebol, mas odeia política.']

for texto in textos:
    for palavra in PALAVRAS:
        if palavra.lower() in texto.lower():
            print('Texto contém uma palavra proibida:', palavra)
            break
    else:
        print('Texto autorizado:', texto)
