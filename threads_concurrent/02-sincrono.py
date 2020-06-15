import time

def any_foo():
    '''
        any_foo é uma função cuja tarefa leva 1 segundo 
        para ser realizada
    '''
    print('sleeping 1 second')
    time.sleep(1)
    print('Feito Sleeping')

#Nesta condição, se eu chamar any_foo duas vezes
#O tempo total de execução será de 2 segundos

inicio = time.perf_counter()
any_foo()
any_foo()
fim = time.perf_counter()

tempo = fim - inicio
print('O tempo de execução foi: ', tempo, 'segundos')

#O que faremos é utilizar o módulo threading para tentar 
#diminuir o tempo de execução

