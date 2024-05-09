array = [64, 34, 25, 12, 22, 11, 90]

def bubble_sort(array):
    n = len(array)
    # Recorre todos los elementos del arreglo
    for i in range(n):
        swapped = False  # Bandera para verificar si se han realizado intercambios
        # Los últimos i elementos ya están en su lugar
        for j in range(0, n-i-1):
            # Recorre el arreglo desde 0 hasta n-i-1
            # Intercambia si el elemento actual es mayor que el siguiente
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True
        # Si no se realizan intercambios, el arreglo ya está ordenado
        if not swapped:
            break



bubble_sort(array)

print("El arreglo ordenado es:", array)

