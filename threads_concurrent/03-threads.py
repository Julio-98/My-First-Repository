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
fim = time.perf_counter()

tempo = fim - inicio
print('O tempo de execução foi: ', tempo, 'segundos')

#Ao rodarmos o código temos uma surpresa, o tempo de execução não
#foi de 1 segundo, mas sim próximo de 0 segundos.
#Isso ocorreu porque após passarmos a segunda thread para o computador
#Não há nada paedindo para que o programa pare de ser executado enquanto 
#As threads estão sendo processadas... Então o programa vai para a pŕoxima linha
#para o cronometro, calcula o tempo, imprime o tempo e espera o retorno das threads
#para encerrar o código. Para resolver isso, usaremos o método join