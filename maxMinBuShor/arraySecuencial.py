array = [6, 14, 1, 18, 10, 8, 5, 11, 16, 15, 2, 12, 4, 7, 19, 13, 9, 3, 20, 17]
search = 11
position = 0
sorted_array=[0]
i=0
def SearchSecuential(array, search):
    for i in range(len(array)):
        if array[i] == search:
            position = i
            print("El elemento", search, "se encuentra en la posición", position)
            break
    else:
        print("Elemento no encontrado")

    return search, array

def selection_sort(array):
    n = len(array)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    
    return array

def SearchBinary(sorted_array, search):
    low = 0
    high = len(sorted_array) - 1
    while low <= high:
        mid = (low + high) // 2
        if sorted_array[mid] == search:
            return mid
        elif sorted_array[mid] < search:
            low = mid + 1
        else:
            high = mid - 1
    return -1  


def main():
    
    print("Su array principal es:",array)
    print("Su numero a buscar es:",search)
    search_result, sorted_array = SearchSecuential(array, search)
    print("Resultado de la búsqueda:", search_result)
    
    sorted_array = selection_sort(array)
    print("Array después de ordenar:", sorted_array)

    
    search_result = SearchBinary(sorted_array, search)
    if search_result != -1:
        print("Elemento encontrado en el índice:", search_result)
    else:
        print("Elemento no encontrado")
main()
