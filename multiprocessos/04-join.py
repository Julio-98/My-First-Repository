#Corrigindo erro "inesperado"
import multiprocessing
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
#criando as dois processos. Observe que não rodamos a função
#apenas passamos ela para um processo
p1 = multiprocessing.Process(target=any_foo)
p2 = multiprocessing.Process(target=any_foo)

#passando o processos para o computador
p1.start()
p2.start()

p1.join()
p2.join()
fim = time.perf_counter()

print('O tempo de execução foi de', fim - inicio,'segundos')
#Agora sim, o tempo de execução foi de um segundo. Isso porque enquanto os dois processos
#não são finalizados o código não continua sendo executado. Não se preocupe muito com isso
#há outra forma de trabalhar commultiprocessos que são mais eficiente, onde não será necessário 
#utilizar o join. Estamos aplicando este método, apenas para
#ter uma noção de como as coisas funcionam por baixo dos panos