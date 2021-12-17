from unidecode import unidecode


def is_one_letter(txt):
    while True:
        text = str(input(txt)).strip().lower()
        if text.isalpha():
            if len(text) == 1:
                return unidecode(text)
            else:
                print('ERRO! Digite apenas uma letra')
        else:
            print('ERRO! Digite uma letra válida')


def readInt(inp="Número inteiro: ", min=0, max=10):
    while True:
        try:
            num = int(input(inp))
            if num in range(min, max):
                return num
            else:
                print('ERRO! Digite uma opção válida!')
        except:
            print('ERRO! Por favor, digite um número inteiro válido.')
