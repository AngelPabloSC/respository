array = [3, 1, 9, 7, 5, 9]

def maxMinFinder(array):
     
    min_val = array [0]  # inicalizamos las variables 
    max_val = array [0]  
    
    for i in array:
        if i < min_val:
            min_val = i  # se actualiza el valor de la variable si el valor de la iteracion es menor que la variable actual
        elif i > max_val:
            max_val = i  # se actualiza el valor de la variable si el valor de la iteracion es mayor que la variable actual
    
    return min_val,max_val

# Llamada a la función maxMinFinder
min_value, max_value = maxMinFinder(array)

# Imprimir los resultados
print("Mínimo:", min_value)
print("Máximo:", max_value)



numeromax=max(array)
numeromis=min(array)
print("mimn",numeromis)
print("max",numeromis)