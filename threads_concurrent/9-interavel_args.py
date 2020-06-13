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
    resultado = [executor.submit(any_foo, seg) for seg in segundos]
#   vamos acessar nosso "encapsulado" e pegar os objetos
#   conforme vão icando prontos    
    for f in concurrent.futures.as_completed(resultado):
        print(f.result())
fim = time.perf_counter()

tempo = fim - inicio
print('O tempo de execução foi: ', tempo, 'segundos')
#Conforme sugerido, independente da ordem em que passamos as threads
#o computador retorna os objetos a medida em que as funções vão
#sendo executadas 