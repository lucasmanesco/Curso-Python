# count é um iterador sem fim

from itertools import count

c1 = count(start=8, step=8)
r1 = range(8, 100, 8)

print('c1 é iterável?', hasattr(c1, '__iter__'))
print('c1 é iterator?', hasattr(c1, '__next__'))

print('r1 é iterável?', hasattr(r1, '__iter__'))
print('r1 é iterator?', hasattr(r1, '__next__'))

print('count')
for i in c1:
    if i >= 100:
        break
    print(i)

print()
print('range')
for i in r1:
    print(i)
