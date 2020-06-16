#vamos ver como isso funciona com o argumentos

import multiprocessing
import time


def any_foo(segundos):
    '''
        any_foo leva 1 segundo para ser executada
    '''
    print('Sleeping', segundos, 'segundo...')
    time.sleep(segundos)
    print('Feito sleeping...')

inicio = time.perf_counter()
#Lista de cada processo criada para posteriormente aplicarmos o join()
processo_list = list()
#criando um loop para 10 processos
for _ in range(10):
#   Por convenção, utilizar o  "_" como variável do for, significa que
#   está variável não será utilizada dentro do loop. Ex. de uma variável 
#   utilizada no loop: "for i in range(10): n = n+i"  
    p = multiprocessing.Process(target=any_foo, args=[1.5])
    p.start()
    processo_list.append(p)

#aplicando o join(). Neste ponto, deve-se entender que colocar o join
#dentro do ultimo loop, faria com que nosso código levasse 10 segundos para
#ser executado. Pois para cada processo, o código ficara parado esperando o retorno
#da função. Em resumo o código estaria funcionando de maneira síncrona.
for processo in processo_list:
    processo.join()
fim = time.perf_counter()

print('O tempo de execução foi de', fim - inicio,'segundos')

#por baixo dos panos, é assim que a coisa acontece.
#Por diante, estaremos mais interessado em ver o apescto prático
#do código.