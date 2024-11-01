DROP DATABASE IF EXISTS Superchino;
CREATE DATABASE Superchino;

USE Superchino;

CREATE TABLE Devoluciones(
DevolucionId INT PRIMARY KEY AUTO_INCREMENT,
ProductoId INT NOT NULL,
CantidadDevuelta INT NOT NULL,
FechaDevolucion DATE NOT NULL
);

CREATE TABLE Inventario(
ProductoId INT PRIMARY KEY AUTO_INCREMENT,
NombreProducto VARCHAR(100) NOT NULL,
Cantidad INT NOT NULL,
Precio DECIMAL(10,2) NOT NULL
);

CREATE TABLE HistorialDevoluciones(
Hist_Id INT PRIMARY KEY AUTO_INCREMENT,
Hist_Date DATE DEFAULT (CURRENT_DATE),
Hist_ProductoId INT NOT NULL,
Hist_CantidadDevuelta INT NOT NULL,
Hist_Fecha_Devolucion DATE
);

INSERT INTO Inventario (ProductoId, NombreProducto, Cantidad, Precio)
VALUES 
('1','Arroz Gallo Largo Fino 1 kg', '50', '2846.00'),
('2','Fideos Spaghetti Matarazzo 500 grs', '300', '1508.00'),
('3','Tomate Perita entero Noel 400 grs', '2000', '980.00'),
('4','Arvejas secas remojadas La Campagnola 300 grs', '850', '836.00'),
('5','Harina de Trigo 000 Cañuelas Refinada 1 Kg', '1500', '687.00'),
('6','Polenta instantánea Harina de maíz Presto Pronta 730 grs', '630', '1293.00'),
('7','Lentejas secas S&P 400 grs', '120', '1550.00'),
('8','Sal fina Dos Anclas paquete 500 grs', '380', '1150.00'),
('9','Queso cremoso Cremón La Serenísima Horma x 3 kgs', '12', '43990.00'),
('10','Leche entera Larga Vida 1 Lt', '100', '1549.00'),
('11','Aceite Cañuelas de Girasol botella 1,5 lts', '95', '3079.00'),
('12','Mate cocido La Tranquera 50 saq', '220', '2100.00'),
('13','Café instantáneo Nescafé Dolca suave frasco 170 grs', '15', '6400.00'),
('14','Pimentón Extra X 500g Saborigal', '9', '5800.00'),
('15','Dulce De Leche La Serenisima Colonial 400 grs', '100', '3120.00'),
('16','Manteca Clasica Sin Tacc La Serenisima Calidad Extra 200g', '63', '4069.00'),
('17','Galletitas Traviata Sabor Original Chica', '400', '483.78'),
('18','Atun Gomes Da Costa Natural Desmenuzado 170 Grs', '28', '3013.00'),
('19','Picadillo 90 Gr Marolio Pate', '12', '2701.00'),
('20','Gaseosa Coca-cola Sabor Original 1,5 Lt', '20', '2199.90');

INSERT INTO Devoluciones(DevolucionId, ProductoId, CantidadDevuelta, FechaDevolucion)
VALUES 
('1','1','5','2024-10-19'),
('2','4','72','2024-10-17'),
('3','7','10','2024-10-12'),
('4','11','5','2024-10-09'),
('5','17','100','2024-10-09'),
('6','20','4','2024-10-02'),
('7','1','10','2024-10-20');

DELIMITER //

DROP PROCEDURE IF EXISTS ProcesarDevoluciones//
CREATE PROCEDURE ProcesarDevoluciones()
BEGIN

	/* Declaracion de las variables para almacenar los valores del FETCH */
	DECLARE fInt_Devolucion INT;
    DECLARE fInt_IDProducto INT;    
    DECLARE fInt_Devuelto INT;
    DECLARE fDate_Fecha DATE;
    
    /* Declaracion de la variable para controlar el ciclo WHILE */
    DECLARE listo INT DEFAULT FALSE;
	
    /* PUNTO 1 de Requisitos. Declaracion del cursor y de la consulta SQL que lo conforma */
    /* Se añaden los campos DevolucionId y FechaDevolucion... */
    /* ...para su inserción posterior en la tabla opcional HistorialDevoluciones*/
    DECLARE cursor_gpo_seis CURSOR FOR 
		SELECT DevolucionId, ProductoId, CantidadDevuelta, FechaDevolucion FROM Devoluciones;     
    
    /* Declaracion de la condición de salida del WHILE */
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET listo = TRUE;

    /* PUNTO 5 de Requisitos. Apertura del cursor*/	
    /* Se abre el cursor para recorrer el conjunto de resultados de la consulta arriba definida */
    OPEN cursor_gpo_seis;
    
    /* PUNTO 2 de Requisitos. Lectura y captura del contenido del primer registro recorrido por el cursor */
    FETCH cursor_gpo_seis INTO fInt_Devolucion, fInt_IDProducto, fInt_Devuelto, fDate_Fecha;
  		   		
    /* PUNTO 2 de Requisitos. Ciclo para cada devolución posterior del primer registro */
    /* Si el primer registro estaba vacío, el ciclo WHILE dará falso y no se ejecutará*/
    WHILE NOT listo DO	
        
        /* PUNTO 2a de Requisitos. Actualización de la cantidad en la tabla Inventario*/
        /* En este punto, se está empleando el contenido del primer registro capturado */
        UPDATE Inventario SET Cantidad = Cantidad + fInt_Devuelto WHERE Inventario.ProductoId = fInt_IDProducto;
        
        /* PUNTO 2b de Requisitos, Opcional. Registro del procesamiento */
        INSERT INTO HistorialDevoluciones (Hist_ProductoId, Hist_CantidadDevuelta, Hist_Fecha_Devolucion)
		VALUES (fInt_IDProducto, fInt_Devuelto, fDate_Fecha); 
        
        /* PUNTO 4 de Requisitos. Eliminación de la devolución, para no repetirla*/
        DELETE FROM Devoluciones WHERE DevolucionId = fInt_Devolucion;        
        
        /* PUNTO 2 de Requisitos. Lectura y captura del contenido del siguiente registro recorrido por el cursor */
        FETCH cursor_gpo_seis INTO fInt_Devolucion, fInt_IDProducto, fInt_Devuelto, fDate_Fecha;
	END WHILE;   
    
    /* PUNTO 5 de Requisitos. Cierre del cursor */	
    CLOSE cursor_gpo_seis;
    
END;
//

/* Ejecución del procedimiento del cursor */	
CALL ProcesarDevoluciones();

/* PUNTO 3 de Requisitos. Consultas SQL para verificar el correcto funcionamiento del cursor */
SELECT Inventario.ProductoId AS Id, NombreProducto AS Producto, Hist_CantidadDevuelta AS Devolucion, Cantidad AS Actualizado 
FROM Inventario INNER JOIN HistorialDevoluciones
WHERE Inventario.ProductoId = HistorialDevoluciones.Hist_ProductoId;

SELECT * FROM HistorialDevoluciones;

SELECT * FROM Devoluciones;
