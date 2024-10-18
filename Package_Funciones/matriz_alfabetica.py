import random
from Package_Matrix import inicializar_matriz,cargar_libros_aleatorios

def biblioteca():
    
    biblio = inicializar_matriz(6,15,"")
    cargar_libros_aleatorios(biblio)

    return biblio