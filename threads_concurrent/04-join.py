import time
import threading

def any_foo():
    '''
        any_foo é uma função cuja tarefa leva 1 segundo 
        para ser realizada
    '''
    print('sleeping 1 second')
    time.sleep(1)
    print('Feito Sleeping')

#criando as duas threads. Observe que não rodamos a função
#apenas passamos ela para uma thread
t1 = threading.Thread(target = any_foo)
t2 = threading.Thread(target = any_foo)

inicio = time.perf_counter()
#passando as threads para o computador 
t1.start()
t2.start()

t1.join()
t2.join()

fim = time.perf_counter()

tempo = fim - inicio
print('O tempo de execução foi: ', tempo, 'segundos')

#Agora sim, o tempo de execução foi de um segundo. Isso por que enquanto as duas thrames não são retornadas, 
#o código não continua sendo executado. Não se preocupe muito com isso
#há outra forma de trabalhar com thrames que são mais eficiente, que não 
#precisaremos utilizar um join. Estamos aplicando este método, apenas para
#ter uma noção de como as coisas funcionam por baixo dos panos
