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
![1](https://github.com/user-attachments/assets/01de1e54-523f-470a-9108-7399695c411a)

### 2. Levantar el servicio con Docker

Abrimos el servicio de Docker, en mi caso uso Docker Desktop y enseguida enviamos el siguiente comando:

```bash
docker-compose up --scale microservicio=2
```
![2](https://github.com/user-attachments/assets/c8479bb1-b1ef-49a6-a15d-13812dbc9b43)

### 3. Obtener una IP pública con Ngrok
Abrimos Ngrok (descargable como aplicación portable) y ejecutamos el siguiente comando para obtener una IP pública. Este comando reemplaza el uso de localhost:8000 por una IP accesible desde cualquier lugar del mundo:

```bash
ngrok http 8000
```
Esta es nuestra IP pública aleatoria:
```bash
https://bfd1-190-110-43-162.ngrok-free.app
```
Nota: Al usar Ngrok en su plan gratuita, cada que iniciemos nuestra aplicación, esta IP cambia. Para este presentación, se deja neustro servicio desplegado por el día 17 de Septiembre de 2024. En caso de pruebas en días psoteriores, esta IP se renovará y actualizará.

![3](https://github.com/user-attachments/assets/81723369-be9a-4096-b539-06820195e356)
![4](https://github.com/user-attachments/assets/57a51a58-1e86-4119-a43e-9ff6f975de4b)

### 4. Endpoint del Microservicio
Nuestro endpoint final será:

```bash
https://bfd1-190-110-43-162.ngrok-free.app/DevOps
```
![5](https://github.com/user-attachments/assets/e304c25e-c15d-41ed-aa14-97b11d575c34)


### 5. Prueba del método POST

![6](https://github.com/user-attachments/assets/4937afdf-1454-436c-bf10-de3dde277b1f)

Finalmente, el microservicio está funcionando correctamente con una IP pública accesible para pruebas.
