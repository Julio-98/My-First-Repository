import time


def any_foo():
    '''
        any_foo leva 1 segundo para ser executada
    '''
    print('Sleeping 1 segundo...')
    time.sleep(1)
    print('Feito sleeping...')

#De maneira síncrona, se eu chamo a função any_foo
#dua vezes o programa levará 2segundos para ser executado

inicio = time.perf_counter()
any_foo()
any_foo()
fim = time.perf_counter()

print('O tempo de execução foi de', fim - inicio,'segundos')

#vejamos quanto tempo leva para a mesma função ser executada 
#duas vezes quando utilizamos multiprocessing