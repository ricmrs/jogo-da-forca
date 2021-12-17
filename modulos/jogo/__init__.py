import modulos.forca as f
from modulos.dados import drawn
from modulos.validacao import is_one_letter
from time import sleep


def game():
    f.title('JOGO DA FORCA', 10)
    categ = f.menu()
    print(f'A categoria selecionada foi {categ.capitalize()}.')
    f.forca()
    word_drawn = drawn(f'dados/{categ}.txt', 'r')

    cont = 0
    guess_list = []
    for w in word_drawn:
        if w == '-':
            guess_list += '-'
        elif w == ' ':
            guess_list += ' '
        else:
            guess_list += '_'
            cont += 1

    print(f'A palavra tem {cont} letras\n')
    print(f'({categ.capitalize()}) Palavra: ' + ''.join(guess_list))

    life = 4
    letters_guessed = ''
    for c in range(0, 4):
        while True:
            letter = is_one_letter(f'Digite uma letra (Chances: {life}) : ')
            if letter not in letters_guessed:
                letters_guessed += letter + ' '
                for k, l in enumerate(word_drawn):
                    if l == letter:
                        guess_list[k] = letter
                word_guess = ''.join(guess_list)
                sleep(0.3)
                print('')
                if letter not in word_drawn:
                    print(f'Errou! A letra {letter} não existe na palavra sorteada.')
                    sleep(0.5)
                    f.forca(c+1)
                    if c != 3:
                        print(f'Letras escolhidas: {letters_guessed}')
                        print(f'Palavra: {word_guess}')
                    else:
                        print('Você perdeu!')
                        print(f'A palavra sorteada era {word_drawn}.')
                    break
                print(f'Acertou! A palavra contém a letra {letter}.')
                if word_guess == word_drawn:
                    print(f'\nParabéns, você ganhou! A palavra era {word_drawn}')
                    break
                print(f'\nLetras escolhidas: {letters_guessed}')
                print(f'({categ.capitalize()}) Palavra: {word_guess}')
            else:
                print(f'Você já digitou a letra {letter}! Digite outra letra.')
        life -= 1
        if word_guess == word_drawn:
            break
