def selection_sort(array):
    n = len(array)
    for i in range(n):
        # Encontrar el índice del elemento mínimo en la parte no ordenada del arreglo
        min_index = i
        for j in range(i + 1, n):
            if array[j] < array[min_index]:
                min_index = j
        
        # Intercambiar el elemento mínimo encontrado con el primer elemento de la parte no ordenada
        array[i], array[min_index] = array[min_index], array[i]
    
    return array

# Ejemplo de uso
array = [64, 25, 12, 22, 11]
sorted_arr = selection_sort(array)
print("Arreglo ordenado de forma ascendente:", sorted_arr)
