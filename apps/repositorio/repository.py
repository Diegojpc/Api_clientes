from db import get_db_connection

class ClienteRepository:
    def crear_cliente(self, cliente):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO clientes (nombre, email, ubicacion) VALUES (%s, %s, %s)',
            (cliente['nombre'], cliente['email'], cliente['ubicacion'])
        )
        conn.commit()
        cursor.close()
        conn.close()
        return cliente

    def leer_clientes(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT idCliente, nombre, email, ubicacion FROM clientes')
        clientes = cursor.fetchall()
        cursor.close()
        conn.close()
        return clientes

    def actualizar_cliente(self, idCliente, cliente):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            'UPDATE clientes SET nombre = %s, email = %s, ubicacion = %s WHERE idCliente = %s',
            (cliente['nombre'], cliente['email'], cliente['ubicacion'], idCliente)
        )
        conn.commit()
        cursor.close()
        conn.close()
        return cliente
    
    def obtener_cliente_por_email(self, email):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM clientes WHERE email = %s"
        cursor.execute(query, (email,))
        cliente = cursor.fetchone()
        cursor.close()
        conn.close()
        return cliente

    def eliminar_cliente(self, idCliente):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM clientes WHERE idCliente = %s', (idCliente,))
        conn.commit()
        cursor.close()
        conn.close()
