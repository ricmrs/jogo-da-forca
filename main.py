from modulos.jogo import game

while True:
    game()
    while True:
        result = str(input('Deseja jogar de novo? [S/N] ')).strip().upper()
        if result in 'SN':
            break
        else:
            print('Valor inválido!')
    if result == 'N':
        break
