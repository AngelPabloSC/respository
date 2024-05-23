import random
import time
# Genera una lista de números aleatorios
def generar_lista(tamano):
    return [random.randint(1, 100) for _ in range(tamano)]

def num_maxAndSum(lista):
    
    numeromaximo=max(lista)
    sumas=sum(lista)
    return numeromaximo,sumas
    
if __name__ == "__main__":
    tamano_lista = 1000
    start_time = time.time() 
    lista = generar_lista(tamano_lista)

    numeromaximo,sumas=num_maxAndSum(lista)
    end_time = time.time() 
    tiempo_transcurrido = end_time - start_time  
    print(f"Su Lista es:{lista}")
    print(f"La suma es:{sumas} y el maximo es{numeromaximo}")
    print(f"Su tiempo es:{tiempo_transcurrido}")