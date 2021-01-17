#!/usr/local/bin/python3

# vai de 1 a 10
for i in range(1, 11):
    print('i = {}'.format(i))

print('\n')

# vai de 0 a 9
for j in range(10):
    print('j = {}'.format(j))

print('\n')

# tabuada
for x in range(1, 11):
    for y in range(1, 11):
        print(f'{x} * {y} = {x * y}')
