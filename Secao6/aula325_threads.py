from threading import Thread
from time import sleep


def vai_demorar(texto, tempo):
    sleep(tempo)
    print(texto)


t1 = Thread(target=vai_demorar, args=('Olá, mundo! (1)', 5))
t1.start()

t2 = Thread(target=vai_demorar, args=('Olá, mundo! (2)', 1))
t2.start()

t3 = Thread(target=vai_demorar, args=('Olá, mundo! (3)', 2))
t3.start()
# t3.join() # se junta à main thread

for i in range(20):
    print(i)
    sleep(.5)

# while t1.is_alive():
#     print('Esperando a Thread 1...')
#     sleep(2)

# print('Thread 1 acabou!')
