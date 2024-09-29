from apps.repositorio.repository import ClienteRepository

class ClienteService:
    def __init__(self):
        self.repo = ClienteRepository()

    def crear_cliente(self, data):
        cliente = {
            'nombre': data['nombre'],
            'email': data['email'],
            'ubicacion': data['ubicacion']
        }
        return self.repo.crear_cliente(cliente)

    def leer_clientes(self):
        return self.repo.leer_clientes()

    def actualizar_cliente(self, idCliente, data):
        cliente = {
            'nombre': data['nombre'],
            'email': data['email'],
            'ubicacion': data['ubicacion']
        }
        return self.repo.actualizar_cliente(idCliente, cliente)
    
    def verificar_cliente(self, email):
        cliente = self.repo.obtener_cliente_por_email(email)
        return cliente is not None

    def eliminar_cliente(self, idCliente):
        return self.repo.eliminar_cliente(idCliente)
