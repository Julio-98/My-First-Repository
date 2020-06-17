import concurrent.futures
import time

def any_foo(segundos):
    '''
        any_foo leva 1 segundo para ser executada
    '''
    print('Sleeping', segundos, 'segundo...')
    time.sleep(segundos)
    return 'Feito sleeping...', segundos



inicio = time.perf_counter()
with concurrent.futures.ProcessPoolExecutor() as executor:
    tempo = [5, 4, 3, 2, 1]
#   utilizando list comprehension
    resultado = [executor.submit(any_foo, s) for s in tempo]
#   vamos acessar nosso "encapsulado" e pegar os objetos
#   conforme vão icando prontos      
    for f in concurrent.futures.as_completed(resultado):
        print(f.result())
fim = time.perf_counter()

print('O tempo de execução foi de', fim - inicio,'segundos')
#Conforme sugerido, independente da ordem em que passamos as threads
#o computador retorna os objetos a medida em que as funções vão
#sendo finalizadas. Assim que um processador fica desocupado, nós
#submetemos outra função ao CPU