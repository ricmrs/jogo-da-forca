from modulos.validacao import readInt


def title(header, leng=0):
    length = len(header) + 4 + leng
    print('-' * length)
    print(f'{header:^{length}}')
    print('-' * length)


def menu():
    categories = ['animais', "objetos", "países", "todos"]
    title('MENU', 16)
    print('1 - Animais')
    print('2 - Objetos')
    print('3 - Países')
    print('4 - Todos')
    print('-' * 20)
    categ = readInt('Escolha uma categoria: ', 1, 5)
    for k, c in enumerate(categories):
        if k == categ - 1:
            return c


def forca(n=0):
    print('-----')
    if n > 0:
        print('|  ( )')
    else:
        print('|')
    if n > 1:
        print('|  /|\\')
    else:
        print('|')
    if n > 2:
        print('|   |')
    else:
        print('|')
    if n > 3:
        print('|  / \\')
    else:
        print('|')
    print('|__')
    print('')
