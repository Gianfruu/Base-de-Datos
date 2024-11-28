
# Sistema de Gestión de hospital


Este documento contiene la justificación del proceso de normalización realizado para el esquema de base de datos **Sistema de Gestión de hospital**, cuya consigna original es la de "Desarrollar un sistema para gestionar un hospital que incluya pacientes, médicos
y turnos de consulta médica".



# 1. Características mínimas cumplidas en el diseño

## Las Entidades y sus tipos

- El diseño tiene tres entidades: "pacientes", "medicos", "turnos" y, en cada caso, se proyecta que:

   - pacientes sea una entidad fuerte, donde cada registro constituya un paciente único, con clave primaria propia e identificatoria.
   - medicos sea una entidad fuerte, donde cada registro constituya un médico único, con clave primaria propia e identificatoria.
   - turnos sea una entidad debil, dependiente de las entidades pacientes y medicos para poder existir.
   - turnos tiene una Clave Primaria compuesta para evitar la duplicación de turnos.



## Atributos, Restricciones de integridad y Cardinalidad

### Entidad pacientes

- **Atributos**: 
   - dni, pa_apellido, pa_nombre, fecha_nacimiento, email, pa_telefono, obra_social, nro_obra_social, domicilio, localidad.

- **Restricciones**:
   - La restricción deseada es la de impedir que se pueda repetir el registro de un mismo paciente.
   - Se crea una PRIMARY KEY, constituida por el dni de cada paciente.
   - Los campos son de tipo NOT NULL, para forzar el ingreso de valores.
   - Cada campo tiene un dominio definido para aceptar un único tipo de datos 


### Entidad medicos

- **Atributos**: 
   - matricula, me_apellido, me_nombre, especialidad, me_telefono.

- **Restricciones**:
   - La restricción deseada es la de impedir que se pueda repetir el registro de un mismo médico.
   - Se crea una PRIMARY KEY, constituida por la matrícula del médico.
   - Los campos son de tipo NOT NULL, para forzar el ingreso de valores. 
   - Cada campo tiene un dominio definido para aceptar un único tipo de datos
   

### Entidad turnos

- **Atributos**: 
   - tr_dni, tr_matricula, tr_fecha, tr_horario

- **Restricciones**:
   - La restricción deseada es que un medico no pueda atender a mas de un paciente para un determinado dia y horario.
   - Se crean dos FOREIGN KEY, a partir del dni de los pacientes y la matrícula de los medicos.
   - Se define como PRIMARY KEY a la combinanción "tr_matricula, tr_fecha, tr_horario", con lo cual se completa la restricción
   - Los campos son de tipo NOT NULL, para forzar el ingreso de valores. 
   - Cada campo tiene un dominio definido para aceptar un único tipo de datos


### Cardinalidades

   - "Un" paciente puede tener "muchos" turnos
   - "Un" medico puede tener "muchos" turnos

## Dependencias Funcionales, Claves Candidatas, Claves Primarias

### Dependencias funcionales

- `dni` produce dependencia funcional de todos los restantes atributos de la tabla "pacientes".
- `matricula` produce dependencia funcional de todos los restantes atributos de la tabla "medicos".
- En la tabla "turnos", `tr_dni`, `tr_fecha`, `tr_horario` es una clave compuesta, con dependencia funcional del atributo `tr_matricula`.

### Claves Candidatas

- El atributo `dni` es clave candidata en la tabla pacientes.
- El atributo `matricula` es clave candidata en la tabla medicos.
- La combinación `(tr_matricula, tr_fecha, tr_horario)` se selecciona como "Clave Primaria" en la tabla "turnos", ya que identifica de forma única la "concesión de un turno, para un paciente en un dia y horario específicos".

### Claves  Primarias

- Se seleccionan las claves candidatas, para su empleo como "Claves Primarias".



## 2. Normalización

### Primera Forma Normal (1FN)

El diseño tiene tres entidades: "pacientes", "medicos", "turnos" y, en cada caso, se verifica que:
- Todas las entidades tienen clave primaria
- Las columnas tiene nombre único dentro de cada entidad.
- Para este diseño además, las nombres de las columnas son unicos para cualquier entidad que se considere.
- Todos los valores para cada campo constituyen entidades no divisibles y/o de tipo único.

### Segunda Forma Normal (2FN)

- Se verifica que todas las entidades cumplen con la 1FN.
- Se verifica que para cada una de las entidades, todos sus campos dependen de la clave primaria

### Tercera Forma Normal (3FN)

- Se verifica que todas las entidades cumplen con la 2FN.
- Se verifica que no hay dependencias transitivas en ningún caso. 

### Esquema Normalizado

1. **Tabla `pacientes`**
   - `dni` (Clave primaria)
   - `pa_apellido`
   - `pa_nombre`
   - `fecha_nacimiento`
   - `email`
   - `pa_telefono`
   - `obra_social`
   - `nro_obra_social`
   - `domicilio`
   - `localidad`

2. **Tabla `medicos`**
   - `matricula` (Clave primaria)
   - `me_apellido`
   - `me_nombre`
   - `especialidad`
   - `me_telefono`      

3. **Tabla `turnos`**
   - `tr_dni` (Clave foránea que referencia a `pacientes`)
   - `tr_matricula` (Clave foránea que referencia a `medicos`)
   - `tr_fecha`
   - `tr_horario`

   - Clave foránea (`tr_dni`) Referencia pacientes(dni),
   - Clave foránea (`tr_matricula`) Referencia medicos(matricula),
   - Clave primaria (`tr_dni`, `tr_fecha`, `tr_horario`)
   - Index: `tr_fecha`



## 3. Descripción de la Base de Datos MySQL

   - Cumple con la solicitud de ser diseñada bajo el paradigma de un modelo relacional.
   - Cumple con la aplicación de las tres Formas Normales básicas para optimizar el diseño. 
   - Cumple con la aplicación de restricciones de integridad para mantener la consistencia de datos.
   - Cumple con implementar operaciones en cascada convenientes para prevenir errores de consistencia.
   - Ejemplo: Se usa ON UPDATE CASCADE, ON DELETE RESTRICT en la tabla turnos, por poseer datos externos.
   - Cumple con hacer uso extendido de consultas avanzadas para recuperar datos.
   - Cumple con utilizar Transacciones y Manejo de errores para garantizar la consistencia de los datos.
   - Ejemplo: se utilizan mecanismos para el manejo de errores, como el uso de `Try:`
   - Ejemplo: se realizaron rigurosas pruebas para garantizar que las operaciones no afectasen a la consistencia.
   - Ejemplo: se minimiza la complejidad y la profundidad alcanzada en las transacciones.
   - Cumple con aplicar Procedimientos Almacenados y Funciones.
   - Ejemplo: se crea una función para verificar el dni ingresado, su tipo, existencia y direccionamiento del pedido.
   - Ejemplo: se crea una función para verificar la matricula ingresada, su tipo, existencia y direccionamiento del pedido.



## 4. Descripción del Sistema de Gestión

   - Cumple con la solicitud de una aplicación en Python que interactúe con la base de datos MySQL. 
   - Cumple con la solicitud de implementar una Interfaz de usuario por Linea de Comandos (CLI).
   - Cumple con la solicitud de poseer las entidades paciente, medico y turnos con fecha y horario
   - El menú propuesto ofrece una flexibilidad mayor que los mínimos solicitados.
   - Se superan holgadamente los cantidades iniciales solicitadas de médicos, pacientes y turnos promedio por paciente.   
   - Se extremaron las previsiones para tratar los errores de los operadores en el ingreso de datos.
   - Se extremaron las medidas para evitar el cierre del programa por fallos al interactuar con MySQL.
   - Se cumple con crear un índice para mejorar el diseño de las consultas más frecuentes, en turnos.


## 5. Consignas para el Menú del CLI

   - GESTION DE PACIENTES: Cumple con registrar, ver y eliminar información de pacientes
   - GESTION DE DOCTORES: Cumple con agregar, actualizar y ver detalles/especialidades de los doctores.
   - GESTION DE DOCTORES: Cumple con mostrar listados de los doctores por apellidos o especialidades.
   - MANEJO DE TURNOS: Cumple con programar, actualizar o cancelar turnos.
   - BUSQUEDAS AVANZADAS: Cumple con buscar pacientes/médicos mediante diferentes atributos.
   - BUSQUEDAS AVANZADAS: Cumple con aceptar texto parcial para nombres y especialidades.
   - REPORTE DE TURNOS: Cumple con una amplia variedad de formas de acceder a los turnos, además de lo solicitado.
   - REPORTE DE TURNOS: Cumple con un reporte de los tres médicos con mas turnos y la cantidad de los turnos.
   - CANCELACION DE TURNOS: Cumple con una amplia variedad de formas de cancelar los turnos.
   - CANCELACION DE TURNOS: Cumple con poder cancelar para un médico dado, desde el médico o desde el paciente.
   - CANCELACION DE TURNOS: Cumple con poder cancelar un rango de fechas, sin importar el orden de ingreso.
