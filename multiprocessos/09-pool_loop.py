#Quando queremos rodar a função várias vezes, o método
#submit deixa de ser eficiente. Vejamos como fazer isso:

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



inicio = time.perf_counter()
with concurrent.futures.ProcessPoolExecutor() as executor:
#   utilizando list comprehension
    resultado = [executor.submit(any_foo, 1) for _ in range(10)]
#   vamos acessar nosso "encapsulado" e pegar os objetos
#   conforme vão icando prontos      
    for f in concurrent.futures.as_completed(resultado):
        print(f.result())
fim = time.perf_counter()

print('O tempo de execução foi de', fim - inicio,'segundos')
#para provar que os objetos são devolvidos conforme vão ficando prontos
#passaremos un interável com diferentes valores como argumento da função
#any_foo no próximo arquivo