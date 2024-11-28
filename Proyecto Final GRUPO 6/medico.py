import mysql.connector

# Conexión a la base de datos
llamada = mysql.connector.connect(
   host="localhost",
   user="root",
   password="segundointento",
   database="hospital"
)

mycursor = llamada.cursor() 




# 31
# Función para mostrar la lista de medicos por apellido
# MENU = "31. Listado de medicos por apellido") 
def mostrar_medicos_apellido():
    try:
        sql = "SELECT * FROM medicos ORDER BY me_apellido"
        mycursor.execute(sql)
        result_set = mycursor.fetchall()
        if mycursor.rowcount == 0:
            print("\nResultado de su consulta: No hay médicos registrados\n")
            input("\nPresione Enter para continuar ")
        else:
            j = 0  
            print("\nListado de médicos, por Apellido\n")
            for i in result_set:                
                j += 1
                print(f"\tMatrícula {i[0]} - {i[1]}, {i[2]} - {i[3]} - {i[4]}")
            print(f"\nTotal de médicos registrados: {j}")
            input("\nPresione Enter para continuar ")
    except mysql.connector.Error as err:
        print("Error al crear la consulta:", err)
        input("\nPresione Enter para continuar ") 
    



# 32
# Función para mostrar la lista de medicos por especialidad") 
# MENU = "32. Listado de medicos por especialidad") 
def mostrar_medicos_especialidad():
    try:
        sql = "SELECT * FROM medicos ORDER BY especialidad"
        mycursor.execute(sql)
        result_set = mycursor.fetchall()
        if mycursor.rowcount == 0:
            print("\nResultado de su consulta: No hay médicos registrados\n")
            input("\nPresione Enter para continuar ")
        else:
            j = 0  
            print("\nListado de médicos, por Especialidad\n")
            for i in result_set:                
                j += 1
                print(f"\tMatrícula {i[0]} - {i[3]} - {i[1]}, {i[2]} - {i[4]}")
            print(f"\nTotal de médicos registrados: {j}")
            input("\nPresione Enter para continuar ")
    except mysql.connector.Error as err:
        print("Error al crear la consulta:", err)
        input("\nPresione Enter para continuar ") 




# 33
# Función para mostrar la lista de medicos por apellido
# MENU = "33. BUSCAR médicos por apellido"
def medicos_por_apellido(apellido: str):
    try:
        sql = f"SELECT * FROM medicos WHERE me_apellido LIKE '%{apellido}%' ORDER BY me_apellido, me_nombre"      
        mycursor.execute(sql)
        result_set = mycursor.fetchall()

        if mycursor.rowcount == 0:
            print(f"\nNo hay médicos para su consulta por apellido '{apellido}'")
            input("\nPresione Enter para continuar ")
        else:
            print(f"\nListado de médicos, para su consulta por apellido '{apellido}'\n")
            j = 0
            for i in result_set:                
                j += 1
                print(f"\tMatrícula {i[0]} - {i[1]}, {i[2]} - {i[3]} - Teléfono {i[4]}")
            print(f"\nTotal de médicos para su consulta por apellido '{apellido}': {j}")
            input("\nPresione Enter para continuar ")
    except mysql.connector.Error as err:
        print("Error al crear la consulta:", err)
        input("\nPresione Enter para continuar ") 




# 34
# Función para mostrar la lista de medicos por especialidad
# MENU = "34. BUSCAR médicos por especialidad"
def medicos_por_especialidad(especialidad: str):
    try:
        sql = f"SELECT * FROM medicos WHERE especialidad LIKE '%{especialidad}%' ORDER BY especialidad, me_apellido"      
        mycursor.execute(sql)
        result_set = mycursor.fetchall()

        if mycursor.rowcount == 0:
            print(f"\nNo hay médicos para su consulta por especialidad '{especialidad}'")
            input("\nPresione Enter para continuar ")
        else:
            print(f"\nListado de médicos, para su consulta por especialidad '{especialidad}'\n")
            j = 0
            for i in result_set:                
                j += 1
                print(f"\t{i[3]} - Matrícula {i[0]} - {i[1]}, {i[2]} - Teléfono {i[4]}")
            print(f"\nTotal de médicos para su consulta por especialidad '{especialidad}': {j}")
            input("\nPresione Enter para continuar ")
    except mysql.connector.Error as err:
        print("Error al crear la consulta:", err)
        input("\nPresione Enter para continuar ") 




# 35.
# Función para Buscar los tres médicos con mas turnos
# MENU = "35. Buscar los Tres médicos con más turnos")
def mostrar_tres_medicos():
    try:
        sql = f"SELECT * FROM turnos"
        mycursor.execute(sql)
        result_set = mycursor.fetchall()
        tiene_turnos = len(result_set)

        if tiene_turnos == 0: 
            print(f"\nResultado de su consulta: No hay turnos registrados")
            input("\nPresione Enter para continuar ")
        elif tiene_turnos >= 1:
            sql2 = f"SELECT tr_matricula, me_apellido, me_nombre, especialidad, COUNT(*) AS total FROM turnos INNER JOIN medicos ON tr_matricula = matricula GROUP BY tr_matricula ORDER BY total DESC, me_apellido"
            mycursor.execute(sql2)
            result_set2 = mycursor.fetchall()
            limite = 3
            resultado = result_set2[:limite]
            print(f"\nListado de los tres médicos con mayor cantidad de turnos\n")
            for i in resultado:
                print(f"\tTotal de turnos: {i[4]} - Matrícula: {i[0]} - Médico: {i[1]} {i[2]} - {i[3]}")  
            
            input("\nPresione Enter para continuar ")

    except mysql.connector.Error as err:
        print("Error al crear la consulta:", err)
        input("\nPresione Enter para continuar ") 




# 36.
# Función para Buscar los tres médicos con mas turnos
# MENU = "36. Cargar un médico nuevo"
def agregar_medico(id_matricula):
    print(f"\n¿Está seguro que desea AGREGAR un médico con la matrícula {id_matricula}?")    
    opcion = input("\nPresione 'S' para Agregar, 'N' para cancelar: ") 
    if opcion.lower() == 's':
        try:
            print(f"\nMatrícula: {id_matricula}")
            new_ape = input("Apellido: ")
            new_nom = input("Nombre: ")
            new_esp = input("Especialidad: ")
            new_tel = input("Teléfono: ")
            sql = f"INSERT INTO medicos(matricula, me_apellido, me_nombre, especialidad, me_telefono) VALUES ('{id_matricula}', '{new_ape}', '{new_nom}', '{new_esp}', '{new_tel}')"
            mycursor.execute(sql)
            llamada.commit()         
            print(f"\nSe agregó un médico con la matrícula {id_matricula} al registro de médicos")
            input("\nPresione Enter para continuar ")
        except mysql.connector.Error as err:
            print("Error al crear la consulta:", err)
            input("\nPresione Enter para continuar ") 
    else:           
        print("\nLa acción fue cancelada")
        input("\nPresione Enter para continuar ")




# 37.
# Función para BORRAR un médico del registro
# MENU = "37. Borrar un médico del registro"

def borrar_medico(id_matricula):
    try:
        sql1 = f"SELECT tr_matricula FROM turnos WHERE tr_matricula={id_matricula}"
        mycursor.execute(sql1)
        result_set1 = mycursor.fetchall()
        tiene_turnos = len(result_set1)
    except mysql.connector.Error as err:
            print("Error al crear la consulta:", err)
            input("\nPresione Enter para continuar ") 

    if tiene_turnos >= 1:
        try:
            sql2 = f"SELECT matricula, me_nombre, me_apellido FROM medicos WHERE matricula={id_matricula}"
            mycursor.execute(sql2)
            result_set2 = mycursor.fetchall()
            print(f"\nEl médico {result_set2[0][2]} {result_set2[0][1]}, matricula {result_set2[0][0]}, tiene turnos programados.")        
            print("Por favor, elimine los turnos de este médico para poder borrarlo.")  
            input("\nPresione Enter para continuar ")       
            return
        except mysql.connector.Error as err:
            print("Error al crear la consulta:", err)
            input("\nPresione Enter para continuar ") 
    elif tiene_turnos == 0:
        try:
            sql2 = f"SELECT matricula, me_nombre, me_apellido FROM medicos WHERE matricula={id_matricula}"
            mycursor.execute(sql2)
            result_set2 = mycursor.fetchall()
            print(f"\n¿Está seguro que desea BORRAR el registro del médico {result_set2[0][2]} {result_set2[0][1]}, matricula {result_set2[0][0]}?")    
            opcion = input("\nPresione 'S' para borrar, 'N' para anular: ") 
            if opcion.lower() == 's':
                sql = f"DELETE FROM medicos WHERE matricula={id_matricula}"
                mycursor.execute(sql)
                llamada.commit()         
                print(f"\nEl médico con matrícula {id_matricula} fue borrado del registro de médicos") 
                input("\nPresione Enter para continuar ")            
            else:           
                print("\nLa acción fue cancelada")
                input("\nPresione Enter para continuar ") 
        except mysql.connector.Error as err:
            print("Error al crear la consulta:", err)
            input("\nPresione Enter para continuar ") 




# 38.
# Función para Actualizar un médico ya registrado
# MENU = "38. Actualizar un médico ya registrado"
def actualizar_medico(id_matricula):
    print(f"\n¿Está seguro que desea MODIFICAR el médico con la matrícula {id_matricula}?")    
    opcion = input("\nPresione 'S' para Modificar, 'N' para cancelar: ") 
    if opcion.lower() == 's':
        try:      
            sql = f"SELECT * FROM medicos WHERE matricula={id_matricula}"
            mycursor.execute(sql)
            result_set = mycursor.fetchall()
            print("\nDatos actuales del médico:")
            for i in result_set:
                print(f"\tMatricula: {i[0]}")
                print(f"\tApellido: {i[1]}")
                print(f"\tNombre: {i[2]}")
                print(f"\tEspecialidad: {i[3]}")     
                print(f"\tTeléfono: {i[4]}")  

            print("\nIngrese los nuevos datos:")
            print(f"\nMatrícula: {id_matricula}")
            new_ape = input("Apellido: ")
            new_nom = input("Nombre: ")
            new_esp = input("Especialidad: ")
            new_tel = input("Teléfono: ")

            sql = "UPDATE medicos SET me_apellido=%s, me_nombre=%s, especialidad=%s, me_telefono=%s WHERE matricula=%s"
            valores = (new_ape, new_nom, new_esp, new_tel, id_matricula)    
            mycursor.execute(sql, valores)
            llamada.commit()         
            print(f"\nSe actualizaron los datos del médico matrícula {id_matricula}")
            input("\nPresione Enter para continuar ")
        except mysql.connector.Error as err:
            print("Error al crear la consulta:", err)
            input("\nPresione Enter para continuar ") 
    else:           
        print("\nLa acción fue cancelada")
        input("\nPresione Enter para continuar ") 




# Función para verificar la matricula
def verificar_matricula(id_matricula:str)->str:
    if id_matricula.isdigit(): 
        try:
            sql = f"SELECT * FROM medicos WHERE matricula={id_matricula}"
            mycursor.execute(sql)
            result_set = mycursor.fetchall()
            registros = len(result_set)
            respuesta = ''
            if registros == 0:
                respuesta = "nada"
                return respuesta 
            elif registros == 1:
                respuesta = "uno"
                return respuesta                             
        except mysql.connector.Error as err:
            print("Error al crear la consulta:", err)
            input("\nPresione Enter para continuar ") 
    else:
        respuesta = "error"
        return respuesta