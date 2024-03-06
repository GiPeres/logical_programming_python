import os

lista = []

while True:
    print('Selecione uma opção:')
    opcao = input('[i]nserir [a]pagar [l]istar')

    if opcao == 'i':
        os.system('cls')
        valor = input('valor: ')
        lista.append(valor)
    elif opcao == 'a':
        indice_str = input('Escolha o indice para apagar:')
        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Não foi possível apagar esse indice!')
        except IndexError:
            print('Indice não existe na lista ainda...')
    elif opcao == 'l':
        os.system('cls')

        if len(lista) == 0:
            print('Não há nada para listar...')

        for i, valor in enumerate(lista):
            print (i, valor)
    else:
        print('Por favor, escolha i, a ou l!')