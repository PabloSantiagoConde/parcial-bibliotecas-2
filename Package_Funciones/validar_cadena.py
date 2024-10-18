def validar_ingreso_alf(elemento) -> str | bool:
    return not tiene_numero(elemento) and tiene_string(elemento)

def tiene_numero(elemento) -> str | bool:
    flag = False
    for i in range(len(elemento)):
        if elemento[i].isnumeric():
            flag = True
    return flag

def tiene_string(elemento) -> str | bool:
    flag = False
    for i in range(len(elemento)):
        if elemento[i].isalpha():
            flag = True
    return flag