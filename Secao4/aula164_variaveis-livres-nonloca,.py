# Variáveis livres + nonlocal

# def fora(x):
#     a = x  # variável livre

#     def dentro():
#         # print(locals())
#         print(dentro.__code__.co_freevars)
#         return a
#     return dentro


# dentro1 = fora(10)
# dentro2 = fora(20)

# print(dentro1())
# print(dentro2())

# print(globals())
# print(locals())

def concatenar(string_inicial):
    valor_final = string_inicial

    def interna(valor_concat=''):
        nonlocal valor_final
        valor_final += valor_concat
        return valor_final
    return interna

c = concatenar('a')
print(c('b'))
print(c('c'))
print(c('d'))
final = c()
print('Final:', final)
