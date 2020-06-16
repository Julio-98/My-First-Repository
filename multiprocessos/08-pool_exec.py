import concurrent.futures
import time


#Perceba que agora any_foo retorna um valor
def any_foo(segundos):
    '''
        any_foo leva 1 segundo para ser executada
    '''
    print('Sleeping', segundos, 'segundo...')
    time.sleep(segundos)
    return 'Feito sleeping...'

#com o executor, tem vários métodos que podemos utilizar
#Para rodar a função uma por vez podemos usar o método submit 
#o método submit, age como se estivessemos agendando uma função 
#para ser executada e retorna um objeto futuro (gerado pela função)
#se quisermos ver esse objeto futuro, podemos pegá-lo com o método result

inicio = time.perf_counter()
with concurrent.futures.ProcessPoolExecutor() as executor:
#   rodando uma por vez
    f1 = executor.submit(any_foo, 1)
    f2 = executor.submit(any_foo, 1)
#   fn = executor.submit(função, argumento)    

#   se quisermos imprimir o retorno das funções, então usamos
#   o método result:
    print(f1.result(), f2.result())
fim = time.perf_counter()

print('O tempo de execução foi de', fim - inicio,'segundos')

#O método concurrent que utilizamos basicamente encapsula a função
#Isso nos permite checar o estádo da mesma, isso é: Se ela está em execução,
#se já foi executada, e até mesmo verificar seu resultado (o que fizemos aqui)
#Contudo, para verificar o objeto futuro, a função tem que retorná-lo
#e é por isso que agora, ao invés de imprimirmos o 'feito sleep'
#retornamos ele como um objeto