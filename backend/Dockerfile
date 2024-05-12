# Utilizar una imagen base de Python 3.9 versión slim para un menor tamaño de imagen
FROM python:3.9-slim

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar el archivo de requisitos primero para aprovechar la caché de Docker
COPY requirements.txt .

# Instalar dependencias usando pip sin guardar la caché para reducir el tamaño de la imagen
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todos los archivos restantes del directorio actual al contenedor
COPY . .

# Exponer el puerto 5000 para permitir el acceso a la aplicación Flask desde fuera del contenedor
EXPOSE 5000

# Definir el comando por defecto para iniciar la aplicación usando Flask
CMD ["flask", "run", "--host=0.0.0.0"]
