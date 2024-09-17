# Usa una imagen base oficial de Python
FROM python:3.10-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos de requirements y el código
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código
COPY . .

# Expone el puerto 8000 para el contenedor
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
