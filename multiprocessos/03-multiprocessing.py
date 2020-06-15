#rodando o mesmo código do arquivo anterior, porém agora com 
#aplicando o método multiprocessing
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

p1.start()
p2.start()

fim = time.perf_counter()

print('O tempo de execução foi de', fim - inicio,'segundos')
#Ao rodarmos o código temos uma surpresa, o tempo de execução não
#foi de 1 segundo, mas sim próximo de 0 segundos.
#Isso ocorreu porque após iniciarmos os processos
#Não há nada pedindo para que o programa pare de ser executado enquanto 
#Os processos estão sendo processadas... Então o programa vai para a pŕoxima linha
#para o cronometro, calcula o tempo, imprime o tempo e espera o retorno dos processos
#Observe que o processo de criar um processo já toma tempo, 
#Então antes mesmo dos processos serem criados, o programa já rodou
#até a última linha
#para encerrar o código. Para resolver isso, usaremos o método join