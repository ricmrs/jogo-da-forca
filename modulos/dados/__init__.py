from random import randint


def num_lines(docum, t):
    doc = open(docum, t)
    total_lines = sum(1 for line in doc)
    doc.close()
    return total_lines


def drawn(docum, t):
    total_words = num_lines(docum, t)
    doc = open(docum, t)
    rand = randint(1, (total_words-1))
    for i, line in enumerate(doc):
        if i == rand:
            drawn = line
            doc.close()
            return drawn.strip().lower()
