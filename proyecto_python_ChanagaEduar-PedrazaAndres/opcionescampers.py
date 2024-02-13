import os
import json

def clear():
    if os.name == 'nt':
        os.system('cls')  # Funcion para limpiar la terminal
    else:
        os.system('clear')


############### Pasar un camper de pre inscrito a inscrito ######################
def inscripcion():
    clear()
    
    # Leer el archivo JSON
    with open('proceso_de_inscripcion.json', 'r') as file:
        datos = json.load(file)
    with open("inscritos.json", "r") as file:
        inscritos = json.load(file)

    # Buscar al pre_inscrito por su número de identificación
    pre_inscritos = datos['campers']['campers_pre_inscritos']
    inscritos = inscritos['campers']['campers_inscritos']

    for pre_inscrito in pre_inscritos:
        print("Numero de identificacion:", pre_inscrito["n_identificacion"], "   Nombre: ",pre_inscrito["Nombre"])
    print("")
    numero_identidad = input("Ingrese la identificacion del camper que desea declarar como inscrito: ")

    for pre_inscrito in pre_inscritos:
        if pre_inscrito['n_identificacion'] == int(numero_identidad):  # Convertir a int
            # Cambiar el estado de proceso de inscripción a inscritos
            pre_inscrito['Estado'] = 'inscritos'
            # Mover el pre_inscrito al nuevo arreglo campers_inscritos
            inscritos.append(pre_inscrito)
            # Remover el pre_inscrito del arreglo campers_pre_inscritos
            pre_inscritos.remove(pre_inscrito)

    # Escribir los cambios de vuelta al archivo JSON
    with open('proceso_de_inscripcion.json', 'w') as file:
        json.dump(datos, file, indent=2)
    with open('inscritos.json', 'w') as file:
        json.dump({"campers": {"campers_inscritos": inscritos}}, file, indent=2)
    



def matriculas():
    print("")




def ingreso_de_notas():
    with open("inscritos.json", "r") as file:
        inscritos = json.load(file)
    with open("aprobados.json","r") as file:
        aprobados=json.load(file)
    
    print("1. Notas de ingreso")
    seleccion_notas = int(input("--> "))

    if seleccion_notas == 1:
        for camper in inscritos['campers']['campers_inscritos']:  # Iterar sobre la lista de campers inscritos
            print("Numero de identificacion:", camper["n_identificacion"], "   Nombre: ",camper["Nombre"])
        identificacion = int(input("Ingrese la identificacion del camper: "))
        for camper in inscritos['campers']['campers_inscritos']:  # Iterar sobre la lista de campers inscritos
            if camper["n_identificacion"] == identificacion:  # Acceder al diccionario de cada camper
                nota_teorica = float(input("Ingrese la nota teorica del camper: "))
                nota_practica = float(input("Ingrese la nota practica del camer: "))
                promedio = (nota_teorica + nota_practica) / 2
                if promedio >=60:
                    camper["Estado"]="aprobado"
                    aprobados["campers"]["campers_aprobados"].append(camper)
                    inscritos['campers']['campers_inscritos'].remove(camper)
                else:
                    camper["Estado"]="reprobado"
                break
        else:
            print("Camper no encontrado")

    with open("inscritos.json", "w") as file:
        json.dump(inscritos, file, indent=4)

    with open("aprobados.json", "w") as file:
        json.dump(aprobados, file, indent=4)