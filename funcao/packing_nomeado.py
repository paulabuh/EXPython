# **kwargs

# Key words args - dicionario
def resultado_f1(**podium):
    for posicao, piloto in podium.items():
        print(f'{posicao} -> {piloto}')


def resultado_f1_(primeiro, segundo, terceiro):
    print(f'1 -> {primeiro}')
    print(f'2 -> {segundo}')
    print(f'3 -> {terceiro}')


if __name__ == '__main__':
    # Packing nomeado
    print(resultado_f1(primeiro='L. Hamilton',
                       segundo='M. Verstappen',
                       terceiro='S. Vettel'))

    # Unpacking nomeado
    podium = {'primeiro': 'L. Hamilton',
              'segundo': 'M. Verstappen',
              'terceiro': 'S. Vettel'}
    resultado_f1_(**podium)
