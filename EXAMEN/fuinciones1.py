# FUNCIONES DE MENU 
def pausar():
    """pausa
    """
    from os import system
    system ("pause")
def limpiar_pantalla():
    """limpia la pantalla de la consola
    """
    from os import system
    system ("cls")
def validar_opcion_menu(opcion):
    
    """
    Valida la opcion ingresada por el usuario.

    Args:
        opcion (str): La opción ingresada por el usuario.

    Returns:
        bool: True si la opción es válida, False en caso contrario.
    """
    if opcion in ["1", "2", "3", "4", "5", "6", "7", "8"]:
        return True
    else:
        print("Opción no válida. Por favor, elija una opción entre 1 y 5.")
        return False
def menu():
    
    """
    Despliega el menu de la app
    """
    print("Bienvenido ")

    print("1.: Se imprimirá por pantalla la tabla con los datos de las bicicletas")
    print("2. Asignar tiempos")
    print("3.Informar ganador")
    print("4. Filtrar por tipo ")
    print("5.Informar promedio por tipo")
    print("7. cambia")
    print("8. cambia")
    print("9. salir ")
    
    eleccion = input("Ingrese su eleccion: ")

    while not validar_opcion_menu(eleccion):
        eleccion = input("Ingrese su eleccion: ")

    return eleccion
#FUNCIONES DE VALIDACION
def validar_lista(lista):
    if not isinstance(lista, list):
        raise ValueError("El argumento debe ser una lista.")
    if len(lista) == 0:
        raise ValueError("La lista no puede estar vacía.")

def extraer_nombre(dic:dict,campo)-> str:
    """extrae un value del diccionario

    Args:
        dic (dict): diccionario del cual extraer algo
        campo (_type_): campo de el cual se desea extraer

    Returns:
        str: retorna el valor del campo solicitado
    """
    return dic.get(campo)

def extraer_cosas(dic:dict,campo0,campo1)-> str:
    """extrae 2 cosa de el diccionario

    Args:
        dic (dict):  diccionario del cual extraer algo
        campo0 (_type_): _campo de el cual se desea extraer
        campo1 (_type_): _campo de el cual se desea extraer

    Returns:
        str: retorna los campos 
    """
     
    return dic.get(campo0,campo1)

#ENCONTRAT MAYORRRRR Y MENORRR
def encontrar_mayor(lista_de_diccios:list,campo:str)-> dict:
    validar_lista(lista_de_diccios)
    """encuentra el mayor de una coleccion de datos

    Args:
        lista_de_diccios (list): la lista a recorrer
        campo (str): el campo con el que compararias el valor SI O SI FLOAT

    Raises:
        ValueError: _si no es un alista

    Returns:
        dict: retorna el "perfil" que cumpla la cpndcion
    """
    if isinstance (lista_de_diccios,list):
        maximo =lista_de_diccios[0]
        for diccionarios in lista_de_diccios:
            if float(diccionarios[campo]) > float(maximo[campo]):
                maximo = diccionarios
    else:
        raise ValueError("nanan flaco es una lista lo que tenes que poner")
    

    return maximo

def encontrar_minimo(lista_de_diccios:list,campo:str)-> dict:
    validar_lista(lista_de_diccios)
    """encuentra el minimop de una coleccion de datos

    Args:
        lista_de_diccios (list): la lista a recorrer
        campo (str): el campo con el que compararias el valor

    Returns:
        dict: retorna el "perfil" que cumpla la cpndcion
    """
    if isinstance (lista_de_diccios,list):
        minimo = lista_de_diccios[0]
        for diccionarios in lista_de_diccios:
            if float(diccionarios[campo]) < float(minimo[campo]):
                minimo = diccionarios
        return minimo
    
########################################################################################
def promedio_de_algo(lista:list,campo )->int:
    validar_lista(lista)
    """saca el promedi de un diccio

    Args:
        lista (list): la lista de la cual sacar el campo
        campo (_type_): lo que se quieras promediar

    Returns:
        int: lo que devuelve xasxmsaubxsyuaivfyutga
    """
    suma_total = 0
    total_de_cosas = len(lista)
    for items in lista:
        suma = float(items[campo])
        suma_total += suma 

    return print(suma_total / total_de_cosas)

#FUNCIONES PARA MAPEAR CAMPO O LISTAS y filtrado
def mapear_campo(lista:list, campo)->list:
    validar_lista(lista)    
    """mapea un campó y muestra todo ese campo en una lsita

    Args:
        lista (list): _lsita a mapear
        campo (_type_): _campo que se desea mapear

    Returns:
        list: la liosta retornada del mapeo_
    """
    lista_retorno = []
    for el in lista:
        lista_retorno.append(el[campo])
    return lista_retorno
def mapear_2_campo(lista:list, campo0:str,campo1:str)->list:
    validar_lista(lista)
    """mapear 2 campos  y devuelve una lsita de lo mapeado 

    Args:
        lista (list): listra con los campo que se desea mapear
        campo0 (str): primer campo a mapear
        campo1 (str): segundo campo a mapear

    Returns:
        list: _description_
    """
    
    lista_retorno = []
    for el in lista:
        lista_retorno.append((el[campo0],el[campo1]))
    return lista_retorno
def mapear_lista(procesadora, lista:list)->list:
    validar_lista(lista)
    """mapea un campo

    Args:
        procesadora (_type_): _una funcion que realiza un aoperacion  de la lista mapeada_
        lista (list): _la lista xd

    Returns:
        list: retorna la lista con el resultado de  la funcion
    """
    lista_retorno = []
    for el in lista:
        lista_retorno.append(procesadora(el))
    return lista_retorno

def filtrar_lista(filtradora, lista:list)->list:
    validar_lista(lista)
    """ filtra la lista

    Args:
        filtradora (_type_): funcion que le pasarias parta que filtre
        lista (list):  lista a validar

    Returns:
        retorna la lista filtrada
    """
    lista_retorno = []
    for el in lista:
        if filtradora(el):
            lista_retorno.append(el)
    return lista_retorno


###################################################################
def agrupar1(lista, campo, campo_agrupar):
    """
    enlista todos los "campo_agrupar" por "campo"

    Args:
        lista (list): lista con un dict 
        campo (str): campo por el que se agrupa
        campo_agrupar (str): campo el cual se agrupa dentro de "campo"

    Returns:
        dict: agrupacion solicitada
    """
    validar_lista(lista)
    campo_retorno = {}
    for el in mapear_lista(lambda el: el[campo], lista):
        campo_retorno[el] = ""
    for i in lista:
        for j in campo_retorno.keys():
            if i[campo] == j:
                campo_retorno[j] += f" {i[campo_agrupar]},"
    return campo_retorno
##########################################################################
#################################################### ordenamaiento de costas
def swap_lista(lista:list, valor1, valor2)->None:
    aux = lista[valor1]
    lista[valor1] = lista[valor2]
    lista[valor2] = aux


def asignar_numeros_ramdom(lista,):
    import random
    lista["tiempo"] = random.randint(50, 120)
    return lista












































