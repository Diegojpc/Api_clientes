CREATE DATABASE IF NOT EXISTS gamma_clientes;

USE gamma_clientes;

CREATE TABLE IF NOT EXISTS clientes (
    idCliente INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    ubicacion VARCHAR(100) NOT NULL
);
