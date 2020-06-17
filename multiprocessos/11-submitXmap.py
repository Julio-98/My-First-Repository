
#A função map é muito utilizada no Python
#map(função, interável), irá passar para função
#cada um dos interáveis como argumento. Quando rodamos isso dentro 
#do modo concurrent.futures.ProcessPoolExecutor(), e passamos map no
#lugar de submit, sem utilizar a ferramenta "as_completed"
#o que teremos como retorno são os objetos na ordem em
#que foram passados, a não na ordem em que foram concluídos.

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
    resultado = executor.map(any_foo, tempo)
    for result in resultado:
        print(result)
fim = time.perf_counter()

print('O tempo de execução foi de', fim - inicio,'segundos')
#Algo importante a ser ressaltado é que o tratamento de exceções 
#Não é realizado durante a execução da função mais sim quando
#Esse dado é recuperado. 