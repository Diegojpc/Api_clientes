# Api_clientes

# API de Gestión de Clientes

Este proyecto es una API desarrollada en Flask para gestionar clientes en una base de datos MySQL. La API permite crear, leer, actualizar, eliminar (CRUD) clientes, así como verificar si un cliente ya está registrado en la base de datos mediante su correo electrónico.

## Estructura del Proyecto

- `cliente_api/app.py`: Archivo principal que inicializa la aplicación Flask.
- `cliente_api/apps/controller/cliente_controller.py`: Controlador que gestiona las rutas de la API relacionadas con los clientes.
- `cliente_api/apps/models/cliente.py`: Modelo SQLAlchemy que representa la tabla `clientes`.
- `cliente_api/apps/repositorio/respository.py`: Repositorio que gestiona las operaciones CRUD en la base de datos.
- `cliente_api/apps/services/cliente_service.py`: Servicio que implementa la lógica de negocio para los clientes.
- `cliente_api/db.py`: Archivo que establece la conexión con la base de datos MySQL.
- `cliente_api/docker-compose.yml`: Configuración de Docker Compose para levantar la aplicación y la base de datos MySQL.
- `cliente_api/Dockerfile`: Archivo Docker para construir la imagen del servicio Flask.
- `cliente_api/init.sql`: Script SQL para inicializar la base de datos `gamma_clientes` y crear la tabla `clientes`.
- `cliente_api/requirements.txt`: Dependencias del proyecto.

## Rutas de la API

### Crear Cliente
- **URL**: `/clientes`
- **Método**: `POST`
- **Descripción**: Crea un nuevo cliente en la base de datos.
- **Body**:
  ```json
  {
    "nombre": "Nombre del Cliente",
    "email": "email@dominio.com",
    "ubicacion": "Ubicación del Cliente"
  }
  ```
- **Respuesta**:
  ```json
  {
    "idCliente": 1,
    "nombre": "Nombre del Cliente",
    "email": "email@dominio.com",
    "ubicacion": "Ubicación del Cliente"
  }
  ```

### Obtener Todos los Clientes
- **URL**: `/clientes`
- **Método**: `GET`
- **Descripción**: Obtiene una lista de todos los clientes registrados.
- **Respuesta**:
  ```json
  [
    {
      "idCliente": 1,
      "nombre": "Nombre del Cliente",
      "email": "email@dominio.com",
      "ubicacion": "Ubicación del Cliente"
    },
    ...
  ]
  ```

### Actualizar Cliente
- **URL**: `/clientes/<int:idCliente>`
- **Método**: `PUT`
- **Descripción**: Actualiza los datos de un cliente existente.
- **Body**:
  ```json
  {
    "nombre": "Nuevo Nombre",
    "email": "nuevo_email@dominio.com",
    "ubicacion": "Nueva Ubicación"
  }
  ```
- **Respuesta**:
  ```json
  {
    "idCliente": 1,
    "nombre": "Nuevo Nombre",
    "email": "nuevo_email@dominio.com",
    "ubicacion": "Nueva Ubicación"
  }
  ```

### Verificar Cliente
- **URL**: `/clientes/verificar`
- **Método**: `POST`
- **Descripción**: Verifica si un cliente con un email específico está registrado en la base de datos.
- **Body**:
  ```json
  {
    "email": "email@dominio.com"
  }
  ```
- **Respuesta**:
  ```json
  {
    "registrado": true
  }
  ```

### Eliminar Cliente
- **URL**: `/clientes/<int:idCliente>`
- **Método**: `DELETE`
- **Descripción**: Elimina un cliente de la base de datos.
- **Respuesta**: Código de estado `204` sin contenido.

## Instalación y Configuración

### Requisitos

- Docker
- Docker Compose
- Python 3.9

### Pasos

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu_usuario/tu_repositorio.git
   cd tu_repositorio
   ```

2. Crea un archivo `.env` basado en el archivo `.env.example` y modifica las credenciales si es necesario:
   ```bash
   MYSQL_ROOT_PASSWORD=tu_password
   MYSQL_DATABASE=gamma_clientes
   MYSQL_USER=root
   MYSQL_PASSWORD=tu_password
   ```

3. Construye y levanta los servicios de la aplicación:
   ```bash
   docker-compose up --build
   ```

4. La API estará disponible en `http://localhost:5001`.

## Uso

### Probar la API

Puedes utilizar [Postman](https://www.postman.com/) o `curl` para interactuar con las rutas de la API.

Ejemplo con `curl` para crear un cliente:
```bash
curl -X POST http://localhost:5001/clientes \
    -H "Content-Type: application/json" \
    -d '{"nombre": "John Doe", "email": "john@example.com", "ubicacion": "New York"}'
```

## Docker

Este proyecto está preparado para ejecutarse con Docker. Utiliza el archivo `docker-compose.yml` para levantar la aplicación y la base de datos MySQL. La aplicación Flask correrá en el puerto `5001` y MySQL en el puerto `3307`.

## Migraciones

El archivo `init.sql` se ejecutará al iniciar la base de datos para crear la base de datos y la tabla `clientes`.

## Dependencias

Las dependencias del proyecto están en el archivo `requirements.txt` e incluyen:

- Flask
- Flask-CORS
- MySQL Connector
- SQLAlchemy
- PyMySQL

## Contribuir

Si deseas contribuir al proyecto, puedes crear un *fork*, trabajar en tus cambios y enviar un *pull request*. ¡Toda contribución es bienvenida!

## Licencia

Este proyecto está licenciado bajo los términos de la licencia MIT.
```

Este `README.md` describe el propósito, las rutas, la configuración y el uso de tu proyecto. Asegúrate de actualizar cualquier URL o detalle según corresponda antes de subirlo a tu repositorio en GitHub.
