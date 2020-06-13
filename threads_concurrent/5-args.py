#com argumentos
import time
import threading

def any_foo(seconds):
    '''
        any_foo é uma função cuja tarefa leva 1 segundo 
        para ser realizada
    '''
    print('sleeping ',seconds,' second(s)')
    time.sleep(seconds)
    print('Feito Sleeping')

inicio = time.perf_counter()
#Lista de cada thread criadas, para posteriormente aplicarmos o join()
threads = list()
#criando um lop com 10 threads
for _ in range(10):
#   Por convenção, utilizar o  "_" como variável do for, significa que
#   está variável não será utilizada dentro do loop. Ex. de uma variável 
#   utilizada no loop: "for i in range(10): n = n+i"
    t = threading.Thread(target = any_foo, args=[1.5])
    t.start()
    threads.append(t)

#aplicando o join(). Neste ponto, deve-se entender que colocar o join
#dentro do ultimo loop, faria com que nosso código levasse 10 segundo para
#ser executado. Pois para cada thread, o código ficara parado esperando o retorno
#da função. Em resumo o código estaria funcionando de maneira síncrona.
for thread in threads:
    thread.join()

fim = time.perf_counter()

tempo = fim - inicio
print('O tempo de execução foi: ', tempo, 'segundos') 

#por baixo dos panos, é assim que a coisa acontece.
#Por diante, estaremos mais interessado em ver o apescto prático
#do código.
