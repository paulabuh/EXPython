#!/usr/local/bin/python3
import csv
from urllib import request


def read(url):
    with request.urlopen(url) as arquivo:
        print('Baixando o arquivo csv...')
        print('Alterando o encode...')
        dados = arquivo.read().decode('latin1')
        for cidade in csv.reader(dados.splitlines()):
            print(f'{cidade[8]}: {cidade[3]}')


# r (raw) antes é str literal, desconsidera \n e outros, usar isso para urls
read(r'http://files.cod3r.com.br/curso-python/desafio-ibge.csv')
