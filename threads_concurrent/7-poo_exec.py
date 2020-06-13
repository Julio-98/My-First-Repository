import time
import concurrent.futures

#perceba que agora any_foo retorna um valor
def any_foo(seconds):
    '''
        any_foo é uma função cuja tarefa leva 1 segundo 
        para ser realizada
    '''
    print('sleeping ',seconds,' second(s)')
    time.sleep(seconds)
    return 'Feito Sleeping'

#com o executor, tem vários métodos que podemos tuilizar
#para rodar a função uma por vez podemos usar o método submit 
#o método submit, age como se estivessemos agendando uma função 
#para ser executada e retorna um objeto futuro (gerado pela função)
#se quisermos ver esse objeto futuro, podemos pegá-lo com o método result

inicio = time.perf_counter()
with concurrent.futures.ThreadPoolExecutor() as executor:
#   rodando uma função por vez    
    f1 = executor.submit(any_foo, 1)
    f2 = executor.submit(any_foo, 1)

#   fn = executor.Thread(função, argumento)
    resultado_futuro = f1.result()
    print(resultado_futuro)
fim = time.perf_counter()

tempo = fim - inicio
print('O tempo de execução foi: ', tempo, 'segundos') 

#O método concurrent que utilizamos basicamente encapsula a função
#O que nos permite checar o estádo da mesma, isso é: Se ela está em execução
#Se já foi executada, verificar seu resultado (o que fizemos aqui)
#Contudo, para verificar o objeto futuro, a função tem que torná-lo
#e é por isso que ao invés de imprimirmos o 'feito sleep'
#retornamos ele como um objeto