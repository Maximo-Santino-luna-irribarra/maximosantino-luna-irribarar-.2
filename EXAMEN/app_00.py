from fuinciones1 import*
import csv
def get_path_actual(nombre_archivo):
    import os
    directorio_actual = os.path.dirname(__file__)
    return os.path.join(directorio_actual, nombre_archivo)

with open(get_path_actual("bicicletas.csv"), "r", encoding="utf-8") as archivo :
    lista_a_trabajar = []
    encabezado = archivo.readline().strip("\n").split(",")#enbabezado es variable onda de la coleccion

    for linea in archivo.readlines():
        persona = {}
        linea = linea.strip("\n").split(",")

        id, nombre, tipo,tiempo = linea
        persona["id_bike"] = int(id)
        persona["nombre"] = nombre
        persona["tipo"] = tipo
        persona["tiempo"] = int(tiempo)
        lista_a_trabajar.append(persona)
    

for i in range(len(lista_a_trabajar)) :
    lista_a_trabajar[i]["nombre"] = lista_a_trabajar[i]["nombre"].upper()

print("----------------------------------------------------")

lista_filtrada = []

for persona in lista_a_trabajar:
    print(persona)

with open(get_path_actual("bicicletas_filtrdas"), "w", encoding="utf-8") as archivo :
    encabezado = ",".join(list(lista_a_trabajar[0].keys())) + "\n"
    archivo.write(encabezado)
    for persona in lista_a_trabajar:
        values = list(persona.values())
        lista_filtrada = []
        for value in values:
            if isinstance(value, int): 
                lista_filtrada.append(str(value))
            elif isinstance(value, float): 
                lista_filtrada.append(str(value))
            else:
                lista_filtrada.append(value)
        linea = ",".join(lista_filtrada) + "\n"
        archivo.write(linea)

    encabezado = ",".join(lista_filtrada) + "\n"

    print(encabezado)
print(lista_a_trabajar)

#menu que muestras todas las funciones
while True:
    limpiar_pantalla()
    match menu():
        case"1":
            print(lista_a_trabajar)

        case"1":
           lista_con_numeros = mapear_lista(asignar_numeros_ramdom,lista_a_trabajar)
           print(lista_con_numeros)

        case"2":
            x  = encontrar_minimo(lista_con_numeros,"tiempo")
            print(f"la persona que gano fue {extraer_nombre(x,"nombre")}")
        case"3":
                 
            lista_con_numeros = mapear_lista(asignar_numeros_ramdom,lista_a_trabajar)
            tipo_bicicleta = input("Ingrese el tipo de bicicleta a filtrar (BMX, Playera, MTB, Paseo): ").upper()
            lista_terminada = filtrar_lista(lambda bici: bici["tipo"] == tipo_bicicleta, lista_con_numeros) 
            with open("bicicletas_mismo_tipo.csv", "w", encoding="utf-8") as archivo:
                archivo.write("nombre,tipo\n")
                for bicicleta in lista_terminada:
                    nombre = bicicleta["nombre"]
                    tipo_bicicletas = bicicleta["tipo"]
                    archivo.write(f"{nombre},{tipo_bicicletas}\n")
        case"4":
                
            tipo_bicicleta = input("Ingrese el tipo de bicicleta a filtrar (BMX, Playera, MTB, Paseo): ").upper()
            lista_final = filtrar_lista(lambda bici: bici["tipo"] == tipo_bicicleta, lista_con_numeros)
            lista_promediada_por_tiempo = promedio_de_algo(lista_final,"tiempo")

        case"5":
            lista_con_numeros = mapear_lista(asignar_numeros_ramdom,lista_a_trabajar)
            lista_filtrada_1= filtrar_lista(lambda bici: bici["tipo"] == "BMX", lista_con_numeros)
            lista_filtrada_2= filtrar_lista(lambda bici: bici["tipo"] == "PLAYERA", lista_con_numeros)
            lista_filtrada_3= filtrar_lista(lambda bici: bici["tipo"] == "MTB", lista_con_numeros)        
            lista_filtrada_4= filtrar_lista(lambda bici: bici["tipo"] == "PASEO", lista_con_numeros)
            lista_promediada_por_tiempo_de_bmx = promedio_de_algo(lista_filtrada_1,"tiempo")
            lista_promediada_por_tiempo_de_playera = promedio_de_algo(lista_filtrada_2,"tiempo")
            lista_promediada_por_tiempo_de_mtb = promedio_de_algo(lista_filtrada_3,"tiempo")
            lista_promediada_por_tiempo_de_paseo = promedio_de_algo(lista_filtrada_4,"tiempo")
            
        case"7":
            pass
        #no me dio timepo
        case"8":
            pass
        #NO ME DIO tiempo
        case"9":
            print("gracias hasta luego")
            break
            
        case _:
            raise ValueError("Debe responder con el numero de una de las opciones vuelva a intentarlo")
    pausar()
