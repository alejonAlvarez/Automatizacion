CREATE DATABASE BancoDB;

USE BancoDB;

CREATE TABLE transacciones (
    id INT IDENTITY(1,1) PRIMARY KEY,
    cliente_id INT,
    nombre VARCHAR(100),
    monto DECIMAL(10,2),
    fecha_transaccion DATETIME DEFAULT GETDATE()
);

INSERT INTO transacciones (cliente_id, nombre, monto)
VALUES 
(101, 'Juan Pérez', 250000.50),
(102, 'María Gómez', 120000.75),
(103, 'Carlos López', 500000.00),
(105, 'Alejandro Alvarez', 800000.00),
(106, 'Brian Estrada', 700000.00),
(107, 'Sara Montoya', 50000.00),
(108, 'Juan Orozco', 10000.00);




select * from transacciones;