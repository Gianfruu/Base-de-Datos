import mysql.connector
from medico import verificar_matricula

# Conexión a la base de datos
llamada = mysql.connector.connect(
   host="localhost",
   user="root",
   password="segundointento",
   database="hospital"
)

mycursor = llamada.cursor() 




# 21.
# Función para mostrar los turnos de un paciente en particular
# MENU = "21. Buscar los turnos de un paciente (dni)"
def turnos_por_paciente(id_dni):
    try:
        sql1 = f"SELECT tr_dni FROM turnos WHERE tr_dni={id_dni}"
        mycursor.execute(sql1)
        result_set1 = mycursor.fetchall()
        tiene_turnos = len(result_set1)
    except mysql.connector.Error as err:
        print("Error al crear la consulta:", err)
        input("\nPresione Enter para continuar ")

    if tiene_turnos == 0:        
        print(f"\nEl paciente {id_dni} no tiene turnos programados.")
        input("\nPresione Enter para continuar ")
    elif tiene_turnos >= 1:
        try:
            sql2 = f"SELECT pa_apellido, pa_nombre, tr_dni, tr_matricula, tr_fecha, tr_horario, me_apellido, especialidad, me_nombre FROM turnos LEFT JOIN pacientes ON tr_dni = dni RIGHT JOIN medicos on tr_matricula = matricula WHERE tr_dni={id_dni} ORDER BY tr_fecha ASC, tr_horario ASC"
            mycursor.execute(sql2)
            result_set2 = mycursor.fetchall()      
            print()
            print(f"TURNOS del Paciente {result_set2[0][1]} {result_set2[0][0]}, Dni {result_set2[0][2]}\n")
            k = 0              
            for i in result_set2:
                k += 1              
                print(f"\t{i[4]}, {i[5]}\tDr {i[3]} {i[6]} {i[8]}, {i[7]}")
            print(f"\nTotal de turnos programados: {k}")
            input("\nPresione Enter para continuar ")
        except mysql.connector.Error as err:
            print("Error al crear la consulta:", err)
            input("\nPresione Enter para continuar ")




# 22.
# CARGAR un turno para un paciente
# MENU = "22. Cargar un turno para un paciente"
def nuevo_turno(id_dni):    
   id_matricula = input("--- Ingrese la matrícula del médico ('x' para volver): ")
   if verificar_matricula(id_matricula) == "uno":
        try:      
            new_fech = input("--- Ingrese la fecha del turno (YYYY-MM-DD), con ese formato: ")
            new_hora = input("--- Ingrese la hora del turno (hh:mm:ss), con ese formato: ")            

            sql = "INSERT INTO turnos(tr_dni, tr_matricula, tr_fecha, tr_horario) VALUES (%s, %s, %s, %s)"
            valores = (id_dni, id_matricula, new_fech, new_hora)
            mycursor.execute(sql, valores)
            llamada.commit()            
            print(f"\nSe CARGÓ un nuevo turno:")
            print(f"\n\t Paciente Dni {id_dni}")
            print(f"\t Médico Matrícula {id_matricula}")
            print(f"\t Fecha: {new_fech}, hora: {new_hora}")
            input("\nPresione Enter para continuar ")
        except mysql.connector.Error as err:
            print("Error al crear la consulta:", err)
            input("\nPresione Enter para continuar ")
   elif verificar_matricula(id_matricula) == "nada":
      print(f"\nLa matrícula {id_matricula} no existe")
      input("\nPresione Enter para continuar ")
      return
   elif verificar_matricula(id_matricula) == "error":
      print("\nERROR: La matrícula debe ser un número entero.")
      input("\nPresione Enter para continuar ")
      return 
    



# 23.
# ACTUALIZAR el turno de un paciente
# MENU = "23. Actualizar el turno de un paciente"
def actualizar_un_turno(id_dni):
    try:        
        sql1 = f"SELECT tr_dni FROM turnos WHERE tr_dni={id_dni}"
        mycursor.execute(sql1)
        result_set1 = mycursor.fetchall()
        tiene_turnos = len(result_set1)
    except mysql.connector.Error as err:
        print("Error al crear la consulta:", err)
        input("\nPresione Enter para continuar ")

    if tiene_turnos == 0:        
        print(f"\nEl paciente {id_dni} no tiene turnos programados.")
        input("\nPresione Enter para continuar ")
    elif tiene_turnos >= 1:
        try:
            sql2 = f"SELECT pa_apellido, pa_nombre, tr_dni, tr_matricula, tr_fecha, tr_horario, me_apellido, especialidad, me_nombre FROM turnos LEFT JOIN pacientes ON tr_dni = dni RIGHT JOIN medicos on tr_matricula = matricula WHERE tr_dni={id_dni} ORDER BY tr_fecha ASC, tr_horario ASC"
            mycursor.execute(sql2)
            result_set2 = mycursor.fetchall()      
            print()
            print(f"TURNOS del Paciente {result_set2[0][1]} {result_set2[0][0]}, Dni {result_set2[0][2]}\n") 

            # Necesito un indice para editar el registro que se seleccione
            # La tabla turnos no tiene un indice autonumérico
            # El indice de la tabla turnos es la combinacion de dni, fecha y horario 
            # Imprimo la lista en pantalla con el índice de la lista
            # 
            editar_indice = []
            K = 0
            for t, i in enumerate(result_set2):
                K += 1             
                print(f"\t'Turno': {t} - {i[4]}, {i[5]}\tDr {i[3]} {i[6]} {i[8]}, {i[7]}")
                editar_indice.append(t)
            
            print(f"\nTotal de turnos programados: {K}")

            # Solicito que se indique cual es el índice del turno a editar       
            registro = input("\na. Por el valor numérico del 'Turno' de la PRIMER columna, ¿Cual registro desea EDITAR? ('x' para salir): ")
            if not registro.isdigit():
                print("\nDebe ingresar un número")
                input("\nPresione Enter para continuar ")
                return 
            
            # Verifico si el Turno seleccionado es parte del listado o se lo inventó   
            # 'valor'será el índice para EDITAR un registro
                        
            elif registro.isdigit():
                valor = int(registro)  
                existe_valor = False               
                for i in editar_indice:
                    if i == valor:
                        existe_valor = True

            # Si el Turno indicado es válido
            if existe_valor: 
                editar_Id = input(f"\nb. ¿Confirma que desea EDITAR el turno {registro}? - 'S' para borrar, 'N' por No: ") 
                if editar_Id.lower() == 's':
                    print("\nIngrese los nuevos datos del turno:")
                    id_matricula = input("--- Ingrese la matrícula del médico ('x' para volver): ")
                    if verificar_matricula(id_matricula) == "uno":                    
                        new_fech = input("--- Ingrese la fecha del turno (YYYY-MM-DD), con ese formato: ")
                        new_hora = input("--- Ingrese la hora del turno (hh:mm:ss), con ese formato: ")

                        for t, i in enumerate(result_set2):
                            if t == valor:                                
                                sql = f"UPDATE turnos SET tr_dni='{id_dni}', tr_matricula='{id_matricula}', tr_fecha='{new_fech}', tr_horario='{new_hora}' WHERE tr_dni='{id_dni}' AND tr_fecha='{i[4]}' AND tr_horario='{i[5]}'"
                                mycursor.execute(sql)
                                llamada.commit()                                 
                                print(f"\nSe ACTUALIZÓ el siguiente Turno:")
                                print(f"\tPACIENTE Dni {id_dni} - {i[1]} {i[0]}")
                                print(f"\tMEDICO matrícula {i[3]} - Fecha/hora {i[4]} {i[5]} - Dr/a {i[6]} {i[8]}, {i[7]}")

                                print(f"\nNUEVOS valores del Turno:")
                                print(f"\tPACIENTE Dni {id_dni} - {i[1]} {i[0]}")
                                try:        
                                    sql3 = f"SELECT me_apellido, me_nombre, especialidad, matricula FROM medicos WHERE matricula='{id_matricula}'"
                                    mycursor.execute(sql3)
                                    result_set3 = mycursor.fetchall()
                                    tiene_turnos = len(result_set3)
                                except mysql.connector.Error as err:
                                    print("Error al crear la consulta:", err)
                                    input("\nPresione Enter para continuar ") 
                                print(f"\tMEDICO matrícula {id_matricula} - Fecha/hora {new_fech} {new_hora} - Dr/a {result_set3[0][0]} {result_set3[0][1]}, {result_set3[0][2]}")

                                input("\nPresione Enter para continuar ") 
                else:
                    print("\nLa acción fue cancelada")
                    input("\nPresione Enter para continuar ")
            else:
                print("\nEl turno no existe o no pertenece al paciente")
                input("\nPresione Enter para continuar ") 
        except mysql.connector.Error as err:
            print("Error al crear la consulta:", err)
            input("\nPresione Enter para continuar ") 



# 24.
# BORRAR un TURNO por un paciente
# MENU = "24. Borrar el turno de un paciente (dni)"
def borrar_un_turno(id_dni):
    try:
        sql1 = f"SELECT tr_dni FROM turnos WHERE tr_dni={id_dni}"
        mycursor.execute(sql1)
        result_set1 = mycursor.fetchall()
        tiene_turnos = len(result_set1)
    except mysql.connector.Error as err:
        print("Error al crear la consulta:", err)
        input("\nPresione Enter para continuar ")

    if tiene_turnos == 0:        
        print(f"\nEl paciente {id_dni} no tiene turnos programados.")
        input("\nPresione Enter para continuar ")
    elif tiene_turnos >= 1:
        try:
            sql2 = f"SELECT pa_apellido, pa_nombre, tr_dni, tr_matricula, tr_fecha, tr_horario, me_apellido, especialidad, me_nombre FROM turnos LEFT JOIN pacientes ON tr_dni = dni RIGHT JOIN medicos on tr_matricula = matricula WHERE tr_dni={id_dni} ORDER BY tr_fecha ASC, tr_horario ASC"
            mycursor.execute(sql2)
            result_set2 = mycursor.fetchall()      
            print()
            print(f"TURNOS del Paciente {result_set2[0][1]} {result_set2[0][0]}, Dni {result_set2[0][2]}\n") 
            
            # Necesito un indice para borrar el registro que se seleccione
            # La tabla turnos no tiene un indice autonumérico
            # El indice de la tabla turnos es la combinacion de dni, fecha y horario 
            # Imprimo la lista en pantalla con el índice de la lista
            # 
            borrar_indice = []
            K = 0
            for t, i in enumerate(result_set2):
                K += 1             
                print(f"\t'Turno': {t} - {i[4]}, {i[5]}\tDr {i[3]} {i[6]} {i[8]}, {i[7]}")
                borrar_indice.append(t)
            print(f"\nTotal de turnos programados: {K}")

            # Solicito que se indique cual es el índice       
            registro = input("\na. Por el valor numérico del 'Turno' de la PRIMER columna, ¿Cual registro desea borrar? ('x' para salir): ")
            if not registro.isdigit():
                print("\nDebe ingresar un número")
                input("\nPresione Enter para continuar ")
                return 
            
            # Verifico si el Turno seleccionado es parte del listado o se lo inventó   
            # 'valor'será el índice para borrar un registro                        
            elif registro.isdigit():
                valor = int(registro)  
                existe_valor = False               
                for i in borrar_indice:
                    if i == valor:
                        existe_valor = True         
            
            # Si el Turno indicado es válido
            if existe_valor: 
                borrarId = input(f"\nb. ¿Confirma que desea BORRAR el turno {registro}? - 'S' para borrar, 'N' por No: ") 
                if borrarId.lower() == 's':
                    for t, i in enumerate(result_set2):
                        if t == valor:                        
                            sql = f"DELETE FROM turnos WHERE tr_dni='{id_dni}' AND tr_matricula = '{i[3]}' AND tr_fecha='{i[4]}' AND tr_horario='{i[5]}'"
                            mycursor.execute(sql)
                            llamada.commit()                        
                            
                            print(f"\nSe BORRÓ el siguiente Turno:")
                            print(f"\tPACIENTE Dni {id_dni} - {i[1]} {i[0]}")
                            print(f"\tMEDICO matrícula {i[3]} - Dr/a {i[6]} {i[8]}, {i[7]}")
                            print(f"\tFecha/hora {i[4]} {i[5]}")
                            input("\nPresione Enter para continuar ")
                else:
                    print("\nLa acción fue cancelada")
                    input("\nPresione Enter para continuar ")
            else:
                print("\nEl turno no existe o no pertenece al paciente")
                input("\nPresione Enter para continuar ")
        except mysql.connector.Error as err:
            print("Error al crear la consulta:", err)
            input("\nPresione Enter para continuar ")




# 25.
# BORRAR TODOS los turnos de un paciente
# MENU = "25. Borrar todos los turnos de un paciente"
def borrar_turnos_paciente(id_dni:int):
    try:
        sql = f"SELECT * FROM turnos WHERE tr_dni={id_dni}"
        mycursor.execute(sql)
        result_set = mycursor.fetchall()
        tiene_turnos = len(result_set)
    except mysql.connector.Error as err:
        print("Error al crear la consulta:", err)
        input("\nPresione Enter para continuar ")    
    if tiene_turnos == 0:        
        print(f"\nEl paciente {id_dni} no tiene turnos programados.")
        input("\nPresione Enter para continuar ")
    elif tiene_turnos >= 1:
        try:
            print(f"\n¿Está seguro que desea BORRAR TODOS los turnos registrados con el Dni {id_dni}?")    
            opcion = input("\nPresione 'S' para borrar, 'N' para anular: ") 
            if opcion.lower() == 's':
                sql = f"DELETE FROM turnos WHERE tr_dni={id_dni}"
                mycursor.execute(sql)
                llamada.commit()
                print(f"\nSe BORRARON TODOS los turnos del Dni {id_dni}")  
                input("\nPresione Enter para continuar ")
            else:
                print("\nLa acción fue cancelada")
                input("\nPresione Enter para continuar ")
        except mysql.connector.Error as err:
            print("Error al crear la consulta:", err)
            input("\nPresione Enter para continuar ")



# 26  
# Función para mostrar los turnos de un médico en particular
# MENU = "26. Buscar los turnos de un médico (matricula)"                
def turnos_por_medico(id_matricula):
    try:
        sql1 = f"SELECT tr_matricula FROM turnos WHERE tr_matricula={id_matricula}"
        mycursor.execute(sql1)
        result_set1 = mycursor.fetchall()
        tiene_turnos = len(result_set1)
    except mysql.connector.Error as err:
            print("Error al crear la consulta:", err)
            input("\nPresione Enter para continuar ") 
        
    if tiene_turnos == 0:
        print(f"\nResultado de su consulta: Este médico no tiene turnos registrados")
        input("\nPresione Enter para continuar ")  
    elif tiene_turnos >= 1:
        try:                      
            sql2 = f"SELECT matricula, me_nombre, me_apellido, especialidad, tr_fecha, tr_horario, dni, pa_apellido, pa_nombre FROM turnos LEFT JOIN medicos ON tr_matricula = matricula RIGHT JOIN pacientes on tr_dni = dni WHERE tr_matricula={id_matricula} ORDER BY tr_fecha ASC, tr_horario ASC"
            mycursor.execute(sql2)
            result_set2 = mycursor.fetchall()

            print(f"\nTURNOS del Médico matrícula {result_set2[0][0]} - {result_set2[0][1]} {result_set2[0][2]}, Especialidad {result_set2[0][3]}, por fecha\n")
            k = 0              
            for i in result_set2:
                k += 1              
                print(f"\t{i[4]}, {i[5]}\t Paciente Dni {i[6]} - {i[7]}, {i[8]}")
            print(f"\nTotal de turnos programados: {k}")
            input("\nPresione Enter para continuar ")
        except mysql.connector.Error as err:
            print("Error al crear la consulta:", err)
            input("\nPresione Enter para continuar ")




# 27
# BORRAR un TURNO por un médico
# MENU = "27. Borrar el turno de un médico (matrícula)"
def borrar_turno_por_medico(id_matricula):
    try:
        sql1 = f"SELECT tr_matricula FROM turnos WHERE tr_matricula={id_matricula}"
        mycursor.execute(sql1)
        result_set1 = mycursor.fetchall()
        tiene_turnos = len(result_set1)
    except mysql.connector.Error as err:
            print("Error al crear la consulta:", err)
            input("\nPresione Enter para continuar ") 
        
    if tiene_turnos == 0:
        print(f"\nResultado de su consulta: Este médico no tiene turnos registrados")
        input("\nPresione Enter para continuar ")  
    elif tiene_turnos >= 1:
        try:                                
            sql2 = f"SELECT matricula, me_nombre, me_apellido, especialidad, tr_fecha, tr_horario, dni, pa_apellido, pa_nombre FROM turnos LEFT JOIN medicos ON tr_matricula = matricula RIGHT JOIN pacientes on tr_dni = dni WHERE tr_matricula={id_matricula} ORDER BY tr_fecha ASC, tr_horario ASC"
            mycursor.execute(sql2)
            result_set2 = mycursor.fetchall()

            print(f"\nTURNOS del Médico matrícula {result_set2[0][0]} - {result_set2[0][1]} {result_set2[0][2]}, Especialidad {result_set2[0][3]}, por fecha.\n")

            # Necesito un indice para borrar el registro que se seleccione
            # La tabla turnos no tiene un indice autonumérico
            # El indice de la tabla turnos es la combinacion de dni, fecha y horario 
            # Imprimo la lista en pantalla con el índice de la lista
            #
            borrar_indice = []
            k = 0              
            for t, i in enumerate(result_set2):
                k += 1              
                print(f"\t'Turno': {t} - {i[4]}, {i[5]}\t Paciente Dni {i[6]} - {i[7]}, {i[8]}")
                borrar_indice.append(t)
            print(f"\nTotal de turnos programados: {k}")

            # Solicito que se indique cual es el índice       
            registro = input("\na. Por el valor numérico del 'Turno' de la PRIMER columna, ¿Cual registro desea borrar? ('x' para salir): ")
            if not registro.isdigit():
                print("\nDebe ingresar un número")
                input("\nPresione Enter para continuar ")
                return 
            
            # Verifico si el Turno seleccionado es parte del listado o se lo inventó   
            # 'valor'será el índice para borrar un registro                        
            elif registro.isdigit():
                valor = int(registro)  
                existe_valor = False               
                for i in borrar_indice:
                    if i == valor:
                        existe_valor = True             
            # Si el Turno indicado es válido
            if existe_valor: 
                borrarId = input(f"\nb. ¿Confirma que desea BORRAR el turno {registro}? - 'S' para borrar, 'N' por No: ") 
                if borrarId.lower() == 's':
                    for t, i in enumerate(result_set2):
                        if t == valor:                        
                            sql = f"DELETE FROM turnos WHERE tr_dni='{i[6]}' AND tr_matricula = '{id_matricula}' AND tr_fecha='{i[4]}' AND tr_horario='{i[5]}'"
                            mycursor.execute(sql)
                            llamada.commit()                        
                            
                            print(f"\nSe BORRÓ el siguiente Turno:")
                            print(f"\tPACIENTE Dni {i[6]} - {i[7]}, {i[8]}")
                            print(f"\tMEDICO matrícula {id_matricula} - Dr/a {i[0]} {i[1]}, {i[2]}")
                            print(f"\tFecha/hora {i[4]} {i[5]}")
                            input("\nPresione Enter para continuar ")
                else:
                    print("\nLa acción fue cancelada")
                    input("\nPresione Enter para continuar ")
            else:
                print("\nEl turno no existe o no pertenece al paciente")
                input("\nPresione Enter para continuar ")
        except mysql.connector.Error as err:
            print("Error al crear la consulta:", err)
            input("\nPresione Enter para continuar ")










# 28.
# BORRAR TODOS los turnos de un medico
# MENU = "28. Borrar todos los turnos de un medico"
def borrar_turnos_medico(id_matricula):
    try:
        sql1 = f"SELECT tr_matricula FROM turnos WHERE tr_matricula={id_matricula}"
        mycursor.execute(sql1)
        result_set1 = mycursor.fetchall()
        tiene_turnos = len(result_set1)
    except mysql.connector.Error as err:
            print("Error al crear la consulta:", err)
            input("\nPresione Enter para continuar ") 
        
    if tiene_turnos == 0:
        print(f"\nResultado de su consulta: Este médico no tiene turnos registrados")
        input("\nPresione Enter para continuar ")
    elif tiene_turnos >= 1:
        try:
            print(f"\n¿Está seguro que desea BORRAR TODOS los turnos del médico matrícula {id_matricula}?")    
            opcion = input("\nPresione 'S' para borrar, 'N' para anular: ") 
            if opcion.lower() == 's':
                sql = f"DELETE FROM turnos WHERE tr_matricula={id_matricula}"
                mycursor.execute(sql)
                llamada.commit()
                print(f"\nSe BORRARON TODOS los turnos del médico matrícula {id_matricula}")  
                input("\nPresione Enter para continuar ")
            else:
                print("\nLa acción fue cancelada")
                input("\nPresione Enter para continuar ")
        except mysql.connector.Error as err:
            print("Error al crear la consulta:", err)
            input("\nPresione Enter para continuar ") 

# 29
# Función para borrar turnos en un rango de fechas
# MENU = "29. Borrar turnos por rango de fechas"
def borrar_turnos_rango_fechas():
    print("\nBORRAR Turnos en un Rango de Fechas, AMBAS INCLUSIVE.")    

    borrar_rango = input(f"\n--- Por favor, CONFIRME - 'S' para Borrar, 'N' por No: ") 

    if borrar_rango.lower() == 's':
        fecha_1 = input("\n--- Ingrese la primer fecha. FORMATO: (YYYY-MM-DD): ")
        fecha_2 = input("--- Ingrese la segunda fecha. FORMATO: (YYYY-MM-DD): ")
        tiene_fecha_1 = len(fecha_1)
        tiene_fecha_2 = len(fecha_2)
        
        if tiene_fecha_1 == 0 or tiene_fecha_2 == 0:
            print("\nDebe ingresar ambas fechas.")
            input("\nPresione Enter para continuar ")
            return
        else:
            try:
                if fecha_1 < fecha_2:                    
                    sql = f"DELETE FROM turnos WHERE tr_fecha BETWEEN '{fecha_1}' AND '{fecha_2}'"                    
                elif fecha_1 > fecha_2:                    
                    sql = f"DELETE FROM turnos WHERE tr_fecha BETWEEN '{fecha_2}' AND '{fecha_1}'"              
                mycursor.execute(sql)
                llamada.commit()                        
                print(f"\nSe BORRARON TODOS los turnos entre el {fecha_1} y el {fecha_2}, ambas fechas inclusive.")
                input("\nPresione Enter para continuar ")
            except mysql.connector.Error as err:
                print("Error al crear la consulta:", err)
                input("\nPresione Enter para continuar ") 
    else:
        print("\nLa acción fue cancelada")
        input("\nPresione Enter para continuar ")