from paciente import *
from medico import *
from turnos import *


# GRUPO 6. ARCE, BARADAD, CAMPAGNUCCI, PELLEGRINI

# SISTEMA DE GESTIÓN DEL HOSPITAL
# Interfaz de usuario

def Gpo6_menu():
    while True:
        print("\n****************************************************************\n")
        print("--- Sistema de Gestión del Hospital ---\n")

        print("*** PACIENTES ***")
        print("11. Buscar paciente por dni")
        print("12. Buscar paciente por apellido")        
        print("13. Cargar un paciente nuevo")
        print("14. Borrar un paciente del registro")
        print("15. Actualizar un paciente ya registrado")
        print("16. Listado de pacientes\n")

        print("*** TURNOS - PACIENTES - DNI ***")
        print("21. Buscar los turnos de un paciente")        
        print("22. Cargar un turno para un paciente")
        print("23. Actualizar el turno de un paciente")
        print("24. Borrar un turno de un paciente")
        print("25. Borrar todos los turnos de un paciente\n") 

        print("*** TURNOS - MEDICOS - MATRICULA ***")
        print("26. Buscar los turnos de un médico")
        print("27. Borrar un turno de un médico")         
        print("28. Borrar todos los turnos de un médico")
        print("29. Borrar turnos por rango de fechas\n")

        print("*** MEDICOS ***")       
        print("31. Listado de medicos (por apellido)")      
        print("32. Listado de medicos (por especialidad)")                
        print("33. Buscar médicos por apellido")
        print("34. Buscar médicos por especialidad")
        print("35. Buscar los Tres médicos con más turnos")
        print("36. Cargar un médico nuevo")
        print("37. Borrar un médico")
        print("38. Actualizar un médico\n")
        print("0. Salir")
        opcion = input("\n\U0001F914 Seleccione una opción: ")
       
        # Se verificará la condición de "entero" del dni, cuando se lo solicite

        if opcion == '11':                
            id_dni = input("\nBUSCAR un paciente por DNI. \n\n--- Ingrese el dni ('x' para volver): ")           
            if verificar_dni(id_dni) == "uno":                               
                mostrar_paciente_dni(int(id_dni))
            elif verificar_dni(id_dni) == "nada":
                print("\nNo hay pacientes con ese dni")
                input("\nPresione Enter para continuar ")
            elif verificar_dni(id_dni) == "error":
                print("\nERROR: El DNI debe ser un número entero.")
                input("\nPresione Enter para continuar ") 
                continue

        elif opcion == '12':  
            str_apellido = input("\nBUSCAR un paciente por apellido. \n\n--- Ingrese el apellido o parte ('x' para volver): ")
            mostrar_paciente_apellido(str_apellido)
        
        elif opcion == '13':
            id_dni = input("\nALTA de un paciente. \n\n--- Ingrese el dni del nuevo paciente ('x' para volver): ")
            if verificar_dni(id_dni) == "uno":
                print(f"\nEl Dni {id_dni} ya existe")
                input("\nPresione Enter para continuar ")
            elif verificar_dni(id_dni) == "error":
                print("\nERROR: El DNI debe ser un número entero.") 
                input("\nPresione Enter para continuar ")
            elif verificar_dni(id_dni) == "nada":     
                agregar_paciente(id_dni)   
                continue
            
        elif opcion == '14':
            id_dni = input("\nBAJA de un paciente. \n\n--- Ingrese el dni ('x' para volver): ")
            if verificar_dni(id_dni) == "uno":   
                borrar_paciente(int(id_dni))
            elif verificar_dni(id_dni) == "nada":
                print(f"\nNo hay pacientes con el dni {id_dni}")
                input("\nPresione Enter para continuar ")
            elif verificar_dni(id_dni) == "error":
                print("\nERROR: El DNI debe ser un número entero.")
                input("\nPresione Enter para continuar ")
                continue 

        elif opcion == '15':
            id_dni = input("\nACTUALIZAR datos de un paciente. \n\n--- Ingrese el dni del paciente ('x' para volver): ")
            if verificar_dni(id_dni) == "nada":
                print(f"\nEl Dni {id_dni} no existe")
                input("\nPresione Enter para continuar ")
            elif verificar_dni(id_dni) == "error":
                print("\nERROR: El DNI debe ser un número entero.")
                input("\nPresione Enter para continuar ") 
            elif verificar_dni(id_dni) == "uno":     
                actualizar_paciente(id_dni)   
                continue
        
        elif opcion == '16':
            mostrar_pacientes()
        
        elif opcion == '21':
            id_dni = input("\nBUSCAR los turnos de un paciente.\n\n--- Ingrese el dni del paciente ('x' para volver): ")
            if verificar_dni(id_dni) == "uno":   
                turnos_por_paciente(int(id_dni))
            elif verificar_dni(id_dni) == "nada":
                print("\nNo hay pacientes con ese dni")
                input("\nPresione Enter para continuar ") 
            elif verificar_dni(id_dni) == "error":
                print("\nERROR: El DNI debe ser un número entero.")
                input("\nPresione Enter para continuar ") 
                continue

        elif opcion == '22':
            id_dni = input("\nCARGAR un Turno para un paciente. \n\n--- Ingrese el dni del paciente ('x' para volver): ")
            if verificar_dni(id_dni) == "uno":
                nuevo_turno(id_dni)                
            elif verificar_dni(id_dni) == "error":
                print("\nERROR: El DNI debe ser un número entero.") 
                input("\nPresione Enter para continuar ")
            elif verificar_dni(id_dni) == "nada":     
                print(f"\nEl Dni {id_dni} no existe")
                input("\nPresione Enter para continuar ")  
                continue
        
        elif opcion == '23':
            id_dni = input("\nACTUALIZAR TURNO de un paciente.\n\n--- Ingrese el dni del paciente ('x' para volver): ")
            if verificar_dni(id_dni) == "uno":   
                actualizar_un_turno(int(id_dni))
            elif verificar_dni(id_dni) == "nada":
                print("\nNo hay pacientes con ese dni")
                input("\nPresione Enter para continuar ")
            elif verificar_dni(id_dni) == "error":
                print("\nERROR: El DNI debe ser un número entero.")
                input("\nPresione Enter para continuar ")
                continue  
        
        elif opcion == '24':
            id_dni = input("\nBORRAR un TURNO de un paciente.\n\n--- Ingrese el dni del paciente ('x' para volver): ")
            if verificar_dni(id_dni) == "uno":   
                borrar_un_turno(int(id_dni))
            elif verificar_dni(id_dni) == "nada":
                print("\nNo hay pacientes con ese dni")
                input("\nPresione Enter para continuar ")
            elif verificar_dni(id_dni) == "error":
                print("\nERROR: El DNI debe ser un número entero.")
                input("\nPresione Enter para continuar ")
                continue 

        elif opcion == '25':
            id_dni = input("\nBORRAR TODOS los turnos de un paciente.\n\n--- Ingrese el dni del paciente ('x' para volver): ")
            if verificar_dni(id_dni) == "uno":   
                borrar_turnos_paciente(int(id_dni))
            elif verificar_dni(id_dni) == "nada":
                print("\nNo hay pacientes con ese dni")
                input("\nPresione Enter para continuar ")
            elif verificar_dni(id_dni) == "error":
                print("\nERROR: El DNI debe ser un número entero.")
                input("\nPresione Enter para continuar ")
                continue

        elif opcion == '26':
            id_matricula = input("\nBUSCAR los turnos de un médico.\n\n--- Ingrese la matricula del médico ('x' para volver): ")
            if verificar_matricula(id_matricula) == "uno":   
                turnos_por_medico(int(id_matricula))
            elif verificar_matricula(id_matricula) == "nada":
                print("\nNo hay médicos con esa matrícula")
                input("\nPresione Enter para continuar ")
            elif verificar_matricula(id_matricula) == "error":
                print("\nERROR: La matrícula debe ser un número entero.")
                input("\nPresione Enter para continuar ")
                continue  

        elif opcion == '27':
            id_matricula = input("\nBORRAR un TURNO de un médico. \n\n--- Ingrese la matrícula del médico ('x' para volver): ")
            if verificar_matricula(id_matricula) == "uno":   
                borrar_turno_por_medico(int(id_matricula))
            elif verificar_matricula(id_matricula) == "nada":
                print(f"\nNo hay un médico con la matrícula {id_matricula}")
                input("\nPresione Enter para continuar ")
            elif verificar_matricula(id_matricula) == "error":
                print("\nERROR: La matrícula debe ser un número entero.")
                input("\nPresione Enter para continuar ")
                continue        
        
        elif opcion == '28':
            id_matricula = input("\nBORRAR TODOS los turnos de un medico.\n\n--- Ingrese la matricula del médico ('x' para volver): ")
            if verificar_matricula(id_matricula) == "uno":   
                borrar_turnos_medico(int(id_matricula))
            elif verificar_matricula(id_matricula) == "nada":
                print("\nNo hay médicos con esa matrícula")
                input("\nPresione Enter para continuar ")
            elif verificar_matricula(id_matricula) == "error":
                print("\nERROR: La matrícula debe ser un número entero.")
                input("\nPresione Enter para continuar ")
                continue 
        
        elif opcion == '29':
            borrar_turnos_rango_fechas()


        elif opcion == '31':
            mostrar_medicos_apellido()
        
        elif opcion == '32':
            mostrar_medicos_especialidad()
        
        elif opcion == '33':  
            str_apellido = input("\nBUSCAR médicos por apellido. \n\n--- Ingrese el apellido o parte ('x' para volver): ")
            medicos_por_apellido(str_apellido)

        elif opcion == '34':  
            especialidad = input("\nBUSCAR médicos por especialidad. \n\n--- Ingrese la especialidad o parte ('x' para volver): ")
            medicos_por_especialidad(especialidad)  
        
        elif opcion == '35':
            mostrar_tres_medicos()
        
        elif opcion == '36':
            id_matricula = input("\nALTA de un médico. \n\n--- Ingrese la matrícula del nuevo médico ('x' para volver): ")
            if verificar_matricula(id_matricula) == "uno":
                print(f"\nLa matrícula {id_matricula} ya existe")
                input("\nPresione Enter para continuar ")
            elif verificar_matricula(id_matricula) == "error":
                print("\nERROR: La matrícula debe ser un número entero.")
                input("\nPresione Enter para continuar ") 
            elif verificar_matricula(id_matricula) == "nada":     
                agregar_medico(id_matricula)   
                continue 

        elif opcion == '37':
            id_matricula = input("\nBAJA de un médico. \n\n--- Ingrese la matrícula del médico ('x' para volver): ")
            if verificar_matricula(id_matricula) == "uno":   
                borrar_medico(int(id_matricula))
            elif verificar_matricula(id_matricula) == "nada":
                print(f"\nNo hay un médico con la matrícula {id_matricula}")
                input("\nPresione Enter para continuar ")
            elif verificar_matricula(id_matricula) == "error":
                print("\nERROR: La matrícula debe ser un número entero.")
                input("\nPresione Enter para continuar ")
                continue    
        
        elif opcion == '38':
            id_matricula = input("\nACTUALIZAR datos de un médico. \n\n--- Ingrese la matrícula del médico ('x' para volver): ")
            if verificar_matricula(id_matricula) == "nada":
                print(f"\nLa matrícula {id_matricula} no existe")
                input("\nPresione Enter para continuar ") 
            elif verificar_matricula(id_matricula) == "error":
                print("\nERROR: La matrícula debe ser un número entero.")
                input("\nPresione Enter para continuar ")  
            elif verificar_matricula(id_matricula) == "uno":     
                actualizar_medico(id_matricula)   
                continue

        elif opcion == '0':
            break

        else:
            print("Opción no válida.")
        
    # Cierre de conexión
    mycursor.close()
    llamada.close()

Gpo6_menu()