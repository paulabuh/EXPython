#!/usr/local/bin/python3
import csv

with open('pessoas.csv') as arquivo:
    for registro in csv.reader(arquivo):
        # pessoa = registro.strip().split(',') # não precisa mais fazer isso
        print('Nome: {}, Idade: {}'.format(*registro))
