# Prueba Técnica para DevOps BP

## Tecnologías utilizadas:

- **Python 3.10** (FastAPI, Uvicorn, Pytest, Httpx)
- **Docker**
- **GitHub Actions** (Pipeline)
- **Ngrok** (Para IP Pública accesible)
- **Postman/HTTPie** (Prueba de método POST)

## Introducción

La resolución de esta prueba está desarrollada en Python con su framework FastAPI para el método POST. El código se encuentra en este repositorio de GitHub e incluye pruebas aplicando TDD y un enfoque de código limpio. A continuación, se detalla su funcionamiento paso a paso.

---

### 1. Clonar el repositorio y activar el ambiente virtual

Una vez clonado o descargado el repositorio, activamos el ambiente virtual con el siguiente comando:

```bash
.\venv\Scripts\activate
```


### 2. Levantar el servicio con Docker

Abrimos el servicio de Docker, en mi caso uso Docker Desktop y enseguida enviamos el siguiente comando:

```bash
docker-compose up --scale microservicio=2
```

### 3. Obtener una IP pública con Ngrok
Abrimos Ngrok (descargable como aplicación portable) y ejecutamos el siguiente comando para obtener una IP pública. Este comando reemplaza el uso de localhost:8000 por una IP accesible desde cualquier lugar del mundo:

```bash
ngrok http 8000
```
```bash
https://bfd1-190-110-43-162.ngrok-free.app
```
### 4. Endpoint del Microservicio
Nuestro endpoint final será:

```bash
https://bfd1-190-110-43-162.ngrok-free.app/DevOps
```

### 5. Prueba del método POST
Finalmente, probamos nuestro método POST usando Postman o HTTPie y verificamos que obtenemos el resultado esperado



Finalmente, el microservicio está funcionando correctamente con una IP pública accesible para pruebas.
