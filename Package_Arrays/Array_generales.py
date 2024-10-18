def valor_max(lista) -> list|int:
    max = float("-inf")                                                         
    
    for i in range(len(lista)):                 
        if lista[i] > max:
            max = lista[i] 
             
    return max   

def valor_min(lista):
    min = float("inf")                                                         
    
    for i in range(len(lista)):                 
        if lista[i] < min:
            min = lista[i] 
             
    return min  

def lista_string(lista):
    string = ""
    for i in range(len(lista)):
        string += lista[i]
    return string

def print_all(lista) -> list:
    for i in range(len(lista)):
        print(lista[i])

def validar_lista(lista): #Verificar si la lista no esta vacía
    return lista != []

def validar_lista_existente(lista):
    if validar_lista(lista):
        return True
    else:
        print("\n Error, antes de realizar esta acción tiene que iniciar la lista (elegir la opción 1) \n")
        return False

def rango(cota_inf,cota_sup,lista):
    lista_nueva = []
    for i in range(len(lista)):
        if cota_inf <= lista[i] <= cota_sup:
            lista_nueva += [lista[i]]
    if validar_lista(lista_nueva):
        return lista_nueva
    else:
        return "No hay numeros en ese rango"

def cantidad_repetidos(lista) -> list | list : #la lsita final debe tener 10 elem
    lista_final = [0] * 10

    for i in range(len(lista)):
        lista_final[lista[i]] += 1
    
    return lista_final

def cargar_columna(columna, lista, matrix): #recibe un columna(int), lista y matriz

    for i in range(len(lista)):
        matrix[i][columna] = lista[i]
    
    return matrix   

def menos_repetido(lista):
    cantidad_min = float("inf")  #caso borde inicial (la cantidad de veces que el n° se repite)
    indice_min = 0               #el numero que sea el minimo
    resultados = [0] * 2        

    for i in range(len(lista)):
        if lista[i] < cantidad_min:
            cantidad_min = lista[i]
            indice_min = i

    resultados[0] = indice_min
    resultados[1] = cantidad_min

    return resultados


def mas_repetido(lista):
    cantidad_max = float("-inf")
    indice_max = 0
    resultados = [0] * 2

    for i in range(len(lista)):
        if lista[i] > cantidad_max:
            cantidad_max = lista[i]
            indice_max = i

    resultados[0] = indice_max
    resultados[1] = cantidad_max

    return resultados


'''        
3. Buscar cuántos números hay de cada uno
1) recorra la lista verificando si el numero en el que estoy parado pertenece solicitado
2) quiero una lista en la que cada indice represente a cada número

3) 

cargar_columna(0, [0,1,2,3,4,5,6,7,8,9,10] , matrix)

[0,1,2,3,4,5,6,7,8,9,10]
||
[0,0]
[1,0]
[2,0]
[3,0]
[4,0]
[5,0]
[6,0]
[7,0]
[8,0]
[9,0]


[4,5,3...]


'''