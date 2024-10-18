from Package_Arrays import lista_string
import random

def inicializar_matriz(filas,columnas,valor_inicial):
    matriz = []
    for i in range(filas):
        fila = [valor_inicial] * columnas

        matriz += [fila] 

    return matriz

def imprimir_matriz(matriz):
    for fila in matriz:
            print(fila) 
    print()
'''

Recorrer la matriz PREVIAMENTE CREADA y en cada indice le carga un sring alfabético en minuscula completamente aleatorio

'''
def cargar_libros_aleatorios(matriz):
    libro = ""
    filas = len(matriz)
    columnas = len(matriz[0])

    for i in range(filas):
        for j in range(columnas):
            
            libro = lista_string(random.choices("abcdefghijklmnopqorstuvwxyz",k=5))
            
            matriz[i][j] = libro

    return matriz