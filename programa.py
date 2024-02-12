# ********************************************
# ********************************************
# Proyecto campuslands "python" 9 de febrero *
# ********************************************
# ********************************************

import json
import uuid
# Abrir el archivo JSON
with open('datos.json', 'r') as datos:
    # Cargar el contenido del archivo en un diccionario
    inscrip = json.load(datos)

with open('datos.json', 'r') as aulas:
    # Cargar el contenido del archivo en un diccionario
    aulas = json.load(aulas)
while True:
    inscritos = inscrip["inscripcion"]["Inscritos"]
    aprobados = inscrip["inscripcion"]["aprobados"]
    reprobados=inscrip["inscripcion"]["reprobados"]
    print("###############")
    print("# Campuslands #")
    print("# Bienvenido! #")
    print("###############")
    print("--------------------")
    print("Que tipo de usuario desea ingresar?")
    print("1. Camper")
    print("2. Trainer")
    print("3. Cordinador")
    Decision1=int(input("--> "))
    print("--------------------")


    ######################### Campers #########################
    if Decision1==1:
        Decision2=0
        while Decision2!=3:
            print("Que desea realizar?")
            print("1. Inscripcion")
            print("2. Ver datos de campers")
            print("3. salir")
            Decision2=int(input("--> "))
            print("--------------------")

            
            if Decision2==1:
                # Obtener el próximo ID disponible
                identificacion_inscripcion=int(input("N° de identificacion: "))
                nombre1_inscrito=str(input("Primer nombre: "))
                nombre2_inscrito=str(input("Segundo nombre: "))
                apellido1_inscrito=str(input("Primero apellido: "))
                apellido2_inscrito=str(input("Segundo apellido: "))
                direccion_inscrito=str(input("Direccion: "))
                acudiente_inscrito=str(input("Nombre acudiente: "))
                celular_inscrito=str(input("Numero celular: "))
                fijo_inscrito=str(input("Numero fijo: "))
                # Nuevo dato a agregar con el próximo ID disponible
                nuevo_dato = {
                    "Id": str(uuid.uuid4()),
                    "n_identificacion": identificacion_inscripcion,
                    "Nombre": nombre1_inscrito+" "+nombre2_inscrito+" "+apellido1_inscrito+" "+apellido2_inscrito,
                    "Direccion": direccion_inscrito,
                    "Acudiente": acudiente_inscrito,
                    "Celular": celular_inscrito,
                    "FIjo": fijo_inscrito,
                    "Estado": "Inscrito"
                }

                # Agregar el nuevo dato a la lista de inscritos
                inscrip["inscripcion"]["Inscritos"].append(nuevo_dato)

                # Escribir el JSON actualizado de vuelta al archivo
                with open('datos.json', 'w') as file:
                    json.dump(inscrip, file, indent=2)









        ######################### Trainers #########################
    if Decision1==2:
        print("")










        ######################### Coordinador #########################
    if Decision1==3:
        decision2=0
        while decision2!=2:
            print("Porfavor digite la contraseña")
            contraseña=str(input("--> "))  #campus2024
            if contraseña=="campus2024":
                print("-----")
                print("Que desea realizar?")
                print("1. Ingresar notas de estudiantes inscritos")
                print("2. salir")
                decision2=int(input("--> "))
                print("-----")


                            #definir si un estudiante inscrito aprueba o reprueba

                if decision2==1: 
                    inscritos_ordenados = sorted(inscritos, key=lambda x: x["Id"])
                    for inscrito in inscritos_ordenados:
                        print("  N° Identificación:", inscrito["n_identificacion"], "  Nombre:", inscrito["Nombre"] )
                    print("-----")
                    identificacion_nota_inscrito=int(input("N° de identificacion del estudiante a ingresar notas: "))
                    nota_teorica_inscrito=float(input("Nota teorica: "))
                    nota_practica_inscrito=float(input("Nota practica: "))
                    calificacion_inscrito=(nota_practica_inscrito+nota_teorica_inscrito)/2
                    for inscrito in inscritos:
                        if inscrito["n-identificacion"] == identificacion_nota_inscrito:
                            # Actualizar el estado del inscrito si la calificación es mayor o igual a 60
                            if calificacion_inscrito >= 60:
                                inscrito["Estado"] = "Aprobado"
                                    # Mover al estudiante de la lista de inscritos a la lista de aprobados
                                    # Generar una nueva ID única para el estudiante aprobado
                                    
                                aprobados.append(inscrito)
                                inscritos.remove(inscrito)
                            else:
                                inscrito["Estado"] = "Reprobado"
                                reprobados.append(inscrito)
                                inscritos.remove(inscrito)
                            break

                        # Escribir el JSON actualizado de vuelta al archivo
                    with open('datos.json', 'w') as file:
                        json.dump(inscrip, file, indent=2)
            else:
                print("contraseña incorrecta")

## Desarrollado por: 
##Eduar Damian Chanaga Gonzalez - 1095581647
##Andres Pedraza Peña - 1005331114