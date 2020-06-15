#A função map é muito utilizada no Python
#map(função, interável), irá passar para função
#cada um dos interáveis como argumento. Quando rodamos isso dentro 
#do modo concurrent.futures.ThreadPoolExecutor(), e passamos map no
#lugar de submit, sem utilizar a ferramente "as_completed"
#o que teremos como retorno são os objetos na ordem em
#que foram passados, a não na ordem em que foram concluídos. 
import time
import concurrent.futures

def any_foo(seconds):
    '''
        any_foo é uma função cuja tarefa leva 1 segundo 
        para ser realizada
    '''
    print('sleeping ',seconds,' second(s)')
    time.sleep(seconds)
    return 'Feito Sleeping', seconds



inicio = time.perf_counter()
with concurrent.futures.ThreadPoolExecutor() as executor:
    segundos = [5, 4, 3, 2, 1]
#   utilizando list comprehension
    resultado = executor.map(any_foo, segundos) 
#   vamos acessar nosso "encapsulado" e pegar os objetos
#   conforme vão icando prontos    
    for result in resultado:
       print(result)
fim = time.perf_counter()

tempo = fim - inicio
print('O tempo de execução foi: ', tempo, 'segundos')

#Algo importante a ser ressaltado é que o tratamento de exceções 
#Não é realizado durante a execução da função mais sim quando
#Esse dado é recuperado. 