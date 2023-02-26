# Introdução às Generator functions em Python
# generator = (n for n in range(1000000))


def generator(n=0, maximum=10):
    # yield 1  # Pausar
    # print('Continuando...')
    # yield 2  # Pausar
    # print('Mais uma...')
    # yield 3 # Pausar
    # print('Terminando...')
    # return 'FIM'
    while True:
        yield n
        n += 1
        if n > maximum:
            return


gen = generator(n=5, maximum=15)
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

for n in gen:
    print(n)
