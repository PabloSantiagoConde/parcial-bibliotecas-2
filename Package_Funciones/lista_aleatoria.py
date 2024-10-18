import random

'''
DATOS IMPORTANTES: 

largo: 100
cant: 0 - 9

EJECUCIÓN: 
    1) crear variable lista e inicializarla (listo)
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    2) cargarle los elementos (Se requiere RECORRIDO -> bucle for )
        3)cada elemento tiene que ser un número aleatorio
    4) devolverme esa lista

'''

def lista_aleatorios():
    
    lista = [0] * 100

    for i in range(len(lista)):
        lista[i] = random.randint(0, 9)
                            ##Solo para int
    return lista

##La responsabilidad de esta funcion es devolverte la lista con n° aleatorios.

