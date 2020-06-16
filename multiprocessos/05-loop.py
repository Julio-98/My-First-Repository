#Muito bem, para termos uma ideia mais consolidada sobre o assunto
#criaremos um loop, executanto a função 10 vezes

import multiprocessing
import time


def any_foo():
    '''
        any_foo leva 1 segundo para ser executada
    '''
    print('Sleeping 1 segundo...')
    time.sleep(1)
    print('Feito sleeping...')

inicio = time.perf_counter()
#Lista de cada processo criada para posteriormente aplicarmos o join()
processo_list = list()
#criando um loop para 10 processos
for _ in range(10):
#   Por convenção, utilizar o  "_" como variável do for, significa que
#   está variável não será utilizada dentro do loop. Ex. de uma variável 
#   utilizada no loop: "for i in range(10): n = n+i"    
    p = multiprocessing.Process(target=any_foo)
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

#Veja que o tempo de execução deste código pode variar de máquina para
#máquina, pois ele depende o Hardware de cda uma. Isso significa que
#idealmente, se eu tenho 10 processadores, ese código levaria aproximadamente
#1 segundo para se executado. Felizmente o contrário não é verdade. Se tenho 
#dois processadores, não significa que a execução do programa levará 5 segundos
#para ser executado, isso graças a um mecanismo de chaveamento dos processadores
#que torna este sistema mais eficiente.