
##El ordenamiento burbuja y dependiendo si el usuario pone ASC o DESC vamos a hacer que se o bien ascendente o bien descendente.


def ordenar_vector(lista,orientacion = "ASC"):

    if orientacion == "ASC":
        for i in range(len(lista)):
            for x in range(0, len(lista) - i - 1):
                if lista[x] > lista[x + 1]:
                    temp = lista[x]
                    lista[x] = lista[x + 1]
                    lista[x + 1] = temp
        return lista
    elif orientacion == "DESC":
        for i in range(len(lista)):
            for x in range(0, len(lista) - i - 1):
                if lista[x] < lista[x + 1]:
                    temp = lista[x]
                    lista[x] = lista[x + 1]
                    lista[x + 1] = temp
    return lista