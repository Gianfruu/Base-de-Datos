import mysql.connector

# Conexión a la base de datos
llamada = mysql.connector.connect(
   host="localhost",
   user="root",
   password="segundointento",
   database="hospital"
)

mycursor = llamada.cursor() 




# 11.
# Función para Buscar un paciente por su dni
# MENU = "11. Solicitar paciente por dni"
def mostrar_paciente_dni(su_dni: int):    
    try:
        sql = f"SELECT * FROM pacientes WHERE dni={su_dni}"
        mycursor.execute(sql)
        result_set = mycursor.fetchall()
        for i in result_set:
            print(f"\nResultado de su consulta: Paciente con el DNI {su_dni}")
            print(f"\tDNI: {i[0]}\n\tApellido y nombre: {i[1]}, {i[2]}\n\tFNac: {i[3]}")
            print(f"\temail: {i[4]}")
            print(f"\tTeléfono: {i[5]}")
            print(f"\tObra Social: {i[6]} - N° {i[7]}")
            print(f"\tDomicilio: {i[8]}. {i[9]}")
            input("\nPresione Enter para continuar ")
    except mysql.connector.Error as err:
        print("Error al crear la consulta:", err)
        input("\nPresione Enter para continuar ")




# 12.
# Función para Buscar un paciente por su apellido o parte del mismo
# MENU = "12. Solicitar paciente por apellido"
def mostrar_paciente_apellido(su_apellido: str):
    try:
        sql = f"SELECT * FROM pacientes WHERE pa_apellido LIKE '%{su_apellido}%'"
        mycursor.execute(sql)
        result_set = mycursor.fetchall()
        registros = len(result_set)

        if registros == 0:
            print(f"\nNo hay pacientes con el apellido '{su_apellido}'")
            input("\nPresione Enter para continuar ")
        else: 
            if registros == 1:                
                for i in result_set: 
                    print(f"\nResultado de su consulta: Paciente con '{su_apellido}' en su apellido\n")
                    print(f"\tDNI: {i[0]}\n\tApellido y nombre: {i[1]}, {i[2]}\n\tFNac: {i[3]}")
                    print(f"\temail: {i[4]}")
                    print(f"\tTeléfono: {i[5]}")
                    print(f"\tObra Social: {i[6]} - N° {i[7]}")
                    print(f"\tDomicilio: {i[8]}. {i[9]}")
                    input("\nPresione Enter para continuar ")
            elif registros > 1:
                j = 0
                print(f"\nResultado de su consulta: 'pacientes con '{su_apellido}' en su apellido'\n")  
                for i in result_set:
                    j += 1
                    #print("\n")                                        
                    print(f"\tDNI: {i[0]}\n\tApellido y nombre: {i[1]}, {i[2]}\n\tFNac: {i[3]}")
                    print(f"\temail: {i[4]}")
                    print(f"\tTeléfono: {i[5]}")
                    print(f"\tObra Social: {i[6]} - N° {i[7]}")
                    print(f"\tDomicilio: {i[8]}. {i[9]}")
                    print("\n")
                
                print(f"Total de pacientes con '{su_apellido}' en su apellido: {j}")
                input("\nPresione Enter para continuar ")

    except mysql.connector.Error as err:
        print("Error al crear la consulta:", err)
        input("\nPresione Enter para continuar ")




# 13.
# Función para cargar un paciente nuevo
# MENU = "13. Cargar un paciente nuevo"
def agregar_paciente(id_dni):
    print(f"\n¿Está seguro que desea AGREGAR un paciente con el Dni {id_dni}?")    
    opcion = input("\nPresione 'S' para Agregar, 'N' para cancelar: ") 
    if opcion.lower() == 's':
        try:
            print(f"\nDni: {id_dni}")
            apellido = input("Apellido: ")
            nombre = input("Nombre: ")
            fnac = input("Fecha de nacimiento (YYYY-MM-DD), con guiones: ")
            email = input("Email: ")
            telefono = input("Teléfono: ")
            obra_social = input("Nombre de la Obra Social: ")
            nro_obra_social = input("Número de Obra Social: ")
            domicilio = input("Domicilio: ")
            localidad = input("Localidad: ")

            sql = f"INSERT INTO pacientes(dni, pa_apellido, pa_nombre, fecha_nacimiento, email, pa_telefono, obra_social, nro_obra_social, domicilio, localidad) VALUES ('{id_dni}', '{apellido}', '{nombre}', '{fnac}', '{email}', '{telefono}', '{obra_social}', '{nro_obra_social}', '{domicilio}', '{localidad}')"
            mycursor.execute(sql)
            llamada.commit()         
            print(f"\nEl paciente con DNI {id_dni} fue agregado al registro de pacientes\n")
            input("\nPresione Enter para continuar ")
        except mysql.connector.Error as err:
            print("Error al crear la consulta:", err)
            input("\nPresione Enter para continuar ")
    else:           
        print("\nLa acción fue cancelada")
        input("\nPresione Enter para continuar ")




# 14.
# Función para borrar un paciente de la lista
# MENU = "14. Borrar un paciente del registro"
def borrar_paciente(id_dni:int):
    try:
        sql1 = f"SELECT tr_dni FROM turnos WHERE tr_dni={id_dni}"
        mycursor.execute(sql1)
        result_set1 = mycursor.fetchall()
        tiene_turnos = len(result_set1)
    except mysql.connector.Error as err:
            print("Error al crear la consulta:", err)
            input("\nPresione Enter para continuar ")

    if tiene_turnos >= 1:
        try:
            sql2 = f"SELECT dni, pa_apellido, pa_nombre FROM pacientes WHERE dni={id_dni}"
            mycursor.execute(sql2)
            result_set2 = mycursor.fetchall()
            print(f"\nEl paciente {result_set2[0][2]} {result_set2[0][1]}, DNI {result_set2[0][0]}, tiene turnos programados.")        
            print("Por favor, elimine los turnos de este paciente para poder borrarlo.")
            input("\nPresione Enter para continuar ")
            return
        except mysql.connector.Error as err:
            print("Error al crear la consulta:", err)
            input("\nPresione Enter para continuar ")
    elif tiene_turnos == 0:
        try:
            sql2 = f"SELECT dni, pa_apellido, pa_nombre FROM pacientes WHERE dni={id_dni}"
            mycursor.execute(sql2)
            result_set2 = mycursor.fetchall()
            print(f"\n¿Está seguro que desea BORRAR el registro del paciente {result_set2[0][2]} {result_set2[0][1]}, DNI {result_set2[0][0]}?")    
            opcion = input("\nPresione 'S' para borrar, 'N' para anular: ") 
            if opcion.lower() == 's':
                sql = f"DELETE FROM pacientes WHERE dni={id_dni}"
                mycursor.execute(sql)
                llamada.commit()         
                print(f"\nEl paciente con DNI {id_dni} fue borrado del registro de pacientes\n")
                input("\nPresione Enter para continuar ")
            else:           
                print("\nLa acción fue cancelada")
                input("\nPresione Enter para continuar ")
        except mysql.connector.Error as err:
            print("Error al crear la consulta:", err)
            input("\nPresione Enter para continuar ")




# 15.
# Función para actualizar un paciente ya registrado
# MENU = "15. Actualizar un paciente ya registrado")
def actualizar_paciente(id_dni):
    print(f"\n¿Está seguro que desea MODIFICAR el paciente con el Dni {id_dni}?")    
    opcion = input("\nPresione 'S' para Modificar, 'N' para cancelar: ") 
    if opcion.lower() == 's':
        try:     
            sql = f"SELECT * FROM pacientes WHERE dni={id_dni}"
            mycursor.execute(sql)
            result_set = mycursor.fetchall()
            print("\nDatos actuales del paciente:")
            for i in result_set:
                print(f"\tDNI: {i[0]}")
                print(f"\tApellido: {i[1]}")
                print(f"\tNombre: {i[2]}")
                print(f"\tFNac: {i[3]}")
                print(f"\temail: {i[4]}")
                print(f"\tTeléfono: {i[5]}")
                print(f"\tObra Social: {i[6]} - N° {i[7]}")
                print(f"\tDomicilio: {i[8]}. {i[9]}")       

            print("\nIngrese los nuevos datos:")
            print(f"Dni: {id_dni}")
            apellido = input("Apellido: ")
            nombre = input("Nombre: ")
            fnac = input("Fecha de nacimiento (YYYY-MM-DD), con guiones: ")
            email = input("Correo electrónico: ")
            telefono = input("Teléfono: ")
            obra_social = input("Nombre de la Obra Social: ")
            nro_obra_social = input("Número de Obra Social: ")
            domicilio = input("Domicilio: ")
            localidad = input("Localidad: ")

            sql = "UPDATE pacientes SET pa_apellido=%s, pa_nombre=%s, fecha_nacimiento=%s, email=%s, pa_telefono=%s, obra_social=%s, nro_obra_social=%s, domicilio=%s, localidad=%s WHERE dni=%s"
            valores = (apellido, nombre, fnac, email, telefono, obra_social, nro_obra_social, domicilio, localidad, id_dni)    
            mycursor.execute(sql, valores)
            llamada.commit()         
            print(f"\nSe actualizaron los datos del paciente Dni {id_dni}\n")
            input("\nPresione Enter para continuar ")
        except mysql.connector.Error as err:
            print("Error al crear la consulta:", err)
            input("\nPresione Enter para continuar ")
    else:           
        print("\nLa acción fue cancelada")
        input("\nPresione Enter para continuar ")




# 16.
# Función para mostrar la lista de pacientes
# MENU = "16. Listado de pacientes"
def mostrar_pacientes():
    try:
        sql = f"SELECT dni, pa_apellido, pa_nombre FROM pacientes ORDER BY pa_apellido"
        mycursor.execute(sql)
        result_set = mycursor.fetchall()
        registros = len(result_set)

        if registros == 0:
            print("\nResultado de su consulta: No hay pacientes registrados\n")
        elif registros >= 1:
            j = 0 
            print("\nResultado de su consulta: Listado de pacientes registrados\n")
            for i in result_set:                
                j += 1
                print(f"\t{i[0]} - {i[1]}, {i[2]}")
            print(f"\nTotal de pacientes registrados: {j}")
            input("\nPresione Enter para continuar ") 
    except mysql.connector.Error as err:
        print("Error al crear la consulta:", err)
        input("\nPresione Enter para continuar ") 




# Función para verificar el dni
def verificar_dni(id_dni:str)->str:
    if id_dni.isdigit(): 
        try:
            sql = f"SELECT * FROM pacientes WHERE dni={id_dni}"
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
    else:
        respuesta = "error"
        return respuesta  