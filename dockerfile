# Usar una imagen base de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar los archivos de requerimientos y las dependencias
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código fuente de la aplicación al contenedor
COPY . .

# Exponer el puerto en el que la aplicación Flask estará corriendo
EXPOSE 5000

# Definir el comando que ejecuta la aplicación
CMD ["sh", "-c", "python db.py && python app.py"]
