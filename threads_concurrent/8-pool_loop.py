#Quando queremos rodar a função várias vezes, o método
#submit deixa de ser eficiente. Vejamos como fazer isso:
import time
import concurrent.futures

def any_foo(seconds):
    '''
        any_foo é uma função cuja tarefa leva 1 segundo 
        para ser realizada
    '''
    print('sleeping ',seconds,' second(s)')
    time.sleep(seconds)
    return 'Feito Sleeping'



inicio = time.perf_counter()
with concurrent.futures.ThreadPoolExecutor() as executor:
#   utilizando list comprehension
    resultado = [executor.submit(any_foo, 1) for _ in range(10)]
#   vamos acessar nosso "encapsulado" e pegar os objetos
#   conforme vão icando prontos    
    for f in concurrent.futures.as_completed(resultado):
        print(f.result)
fim = time.perf_counter()

tempo = fim - inicio
print('O tempo de execução foi: ', tempo, 'segundos') 
#para provar que os objetos são devolvidos conforme vão ficando prontos
#passaremos un interável com diferentes valores como argumento da função
#any_foo no próximo arquivo.