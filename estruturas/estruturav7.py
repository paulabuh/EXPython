#!/usr/local/bin/python3

for x in range(1, 11):
    if x % 2 == 0:
        continue  # interrompe o for e passa para o proximo
    print(x)

for x in range(1, 11):
    if x == 5:
        break
    print(x)

for i in range(1, 11):
    if i == 6:
        break  # não executa o else quanto tem o break
    print(i)
else:
    print('Fim do for')
