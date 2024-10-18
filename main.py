from Package_Funciones import *
from Package_Input import *
from Package_Matrix import *
from Package_Arrays import *


#0) Inicializar el bucle
#1) Pedirle al usuario una opcion
#2) Validar la opción de que sea válida
#3) Hago lo que la opcion me pida (si se puede)

def biblioteca_moreno():

    lista = []
    NUMEROS_POSIBLES = [0,1,2,3,4,5,6,7,8,9]

    while True:

        opcion = get_int("Bienvenido a la biblioteca Moreno. Seleccione la opción que solicita. \n 1.Generar lista de numeros aleatorios \n 2.Ordenar la lista previamente creada \n 3.Buscar e informar cuantas veces se repite cada uno de los números del 0 al 9. \n 4. Ver los numeros que mas se repiten y los que menos se repiten \n 5. Generar la matriz aleatoria \n 6.Ingresar palabra \n 7.Salir \n Ingrese la opcion deseada:","Error, opcion inexistente",1,7,50)

        match opcion:
            case 1:
                lista = lista_aleatorios()
                print(f"\n La lista de numeros creada es: {lista} \n ")
            case 2:
                if validar_lista_existente(lista):
                    orientacion = get_str("\n Ingrese la orientación del vector: ASC|DESC: ","Error, opcion fuera de rango",4).upper()
                    print(f"\n El vector solicitado en orden {orientacion} es: \n{ordenar_vector(lista,orientacion)}\n")
            case 3:
                if validar_lista_existente(lista):
                    print("\n INFORME DE REPETIDOS \n NUMERO | CANTIDAD")
                    tabla_resultados = inicializar_matriz(10,2,0)
                    cargar_columna(0,NUMEROS_POSIBLES,tabla_resultados)
                    cargar_columna(1,cantidad_repetidos(lista),tabla_resultados)
                    imprimir_matriz(tabla_resultados)
                    print()
            case 4:
                if validar_lista_existente(lista):
                    print(f"\n El número que más se repite es el {mas_repetido(cantidad_repetidos(lista))[0]} con cantidad {mas_repetido(cantidad_repetidos(lista))[1]} y el menos repetido es {menos_repetido(cantidad_repetidos(lista))[0]} con cantidad {menos_repetido(cantidad_repetidos(lista))[1]} \n")
            case 5:
                imprimir_matriz(biblioteca())
            case 6:
                cadena = get_str("\n Ingrese una cadena de texto: ","\n Error rango excedido \n",500000)
                if validar_ingreso_alf(cadena):
                    print(f"\n Mensaje cargado correctamente {cadena} \n")
                else: 
                    print(f"\n ERROR: El mensaje no tiene que tener caracteres numericos \n")
            case 7:
                break
            
biblioteca_moreno()




