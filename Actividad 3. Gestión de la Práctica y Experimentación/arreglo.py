
import random
import time
# Genera una lista de números aleatorios
def generar_lista(tamano):
    return [random.randint(1, 100) for _ in range(tamano)]

# Encuentra el elemento máximo en la lista
def encontrar_maximo(lista):
    maximo = lista[0]
    for num in lista:
        if num > maximo:
            maximo = num
    return maximo

# Suma todos los elementos en la lista
def sumar_elementos(lista):
    suma = 0
    for num in lista:
        suma += num
    return suma

# Main
if __name__ == "__main__":

   
    tamano_lista = 1000
    start_time = time.time() 
    lista = generar_lista(tamano_lista)
    maximo = encontrar_maximo(lista)
    suma = sumar_elementos(lista)
    end_time = time.time() 
    tiempo_transcurrido = end_time - start_time  
    print(f"Lista: {lista}")
    print(f"Máximo: {maximo}")
    print(f"Suma: {suma}")
    print(f"Tiempo transcurrido: {tiempo_transcurrido} segundos")