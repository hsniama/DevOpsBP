# Prueba Técnica para DevOps BP

## Tecnologías utilizadas:

- **Python 3.10** (FastAPI, Uvicorn, Pytest, Httpx, pyjwt)
- **Docker**
- **GitHub Actions** (Pipeline)
- **Ngrok** (Para IP Pública accesible)
- **Postman/HTTPie** (Prueba de método POST)

## Insumos para probar código

URL pública:
```bash
https://db3b-190-110-43-162.ngrok-free.app/DevOps
```
JWT:

```bash
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzb21lIjoiZGF0YSJ9.6MfNTlGqkNeN7ZcJHjFGijNzuvUporWTid7W38PBzWc
```

Link de este repositorio:

```bash
https://github.com/HenryNiama/DevOpsBP
```

## Introducción

La resolución de esta prueba está desarrollada en Python con su framework FastAPI para el método POST. El código se encuentra en este repositorio de GitHub e incluye pruebas aplicando TDD y un enfoque de código limpio. A continuación, se detalla su funcionamiento paso a paso.

---

### 1. Clonar el repositorio y activar el ambiente virtual

Una vez clonado o descargado el repositorio, activamos el ambiente virtual con el siguiente comando:

```bash
.\venv\Scripts\activate
```
![1](https://github.com/user-attachments/assets/521144c6-a0bb-4029-8caa-e4ed3d1b6f84)

### 2. Levantar el servicio con Docker

Abrimos el servicio de Docker, en mi caso uso Docker Desktop y enseguida enviamos el siguiente comando:

```bash
docker-compose up --scale microservicio=2
```
![2](https://github.com/user-attachments/assets/ebe08a00-aa22-4dc6-ab21-4f1f024538f3)

![2 2](https://github.com/user-attachments/assets/2cc3d323-5f12-4434-8653-2de7141fe00f)

### 3. Obtener una IP pública con Ngrok
Ejecutamos el siguiente comando de docker para ver si estan corriendo los cointainers y para conocer el puerto de cada una
de las 2 replicas configuradas.

```bash
docker ps
```
![3](https://github.com/user-attachments/assets/35d92323-5ce4-4cc4-92ad-0ad67da34d4f)

Después, copiamos cualquiera de los dos puertos y abrimos Ngrok (descargable como aplicación portable, es una consola) y ejecutamos el siguiente comando para obtener una IP pública. Este comando reemplaza el uso de localhost:8000 por una IP accesible desde cualquier lugar del mundo:

```bash
ngrok http (puerto elegido)
```
![3 1](https://github.com/user-attachments/assets/f11fb44d-eeb1-4fa8-aba5-5bc53929511b)

Esta es nuestra IP pública aleatoria como se observa en la imagen:

![3 2](https://github.com/user-attachments/assets/fcc1e154-39f7-44f1-ba86-0799190fed94)

```bash
https://db3b-190-110-43-162.ngrok-free.app
```
Nota: Al usar Ngrok en su plan gratuito, cada que iniciemos nuestra aplicación, esta IP cambia. Para este presentación, se deja nuestro servicio desplegado por todo el día 18 de Septiembre de 2024. En caso de pruebas en días posteriores, esta IP se renovará y se actualizará en este repositorio.

![3](https://github.com/user-attachments/assets/81723369-be9a-4096-b539-06820195e356)
![4](https://github.com/user-attachments/assets/57a51a58-1e86-4119-a43e-9ff6f975de4b)


### 4. Endpoint del Microservicio
Nuestro endpoint final será:

```bash
https://db3b-190-110-43-162.ngrok-free.app/DevOps
```

Esta URL la copiamos en un navegador.

![4](https://github.com/user-attachments/assets/0a2601db-188a-4f6c-8ae8-e86d569a948c)
![4 1](https://github.com/user-attachments/assets/27121c4c-6d5f-4280-bd11-abde1a3ac979)


### 5. Prueba del método POST

Finalmente, usamos POSTMAN o cualquier otro testeador de métodos, en mi caso uso HTTPie, y configuramos las cabeceras:

![5](https://github.com/user-attachments/assets/d9ccf1f4-e872-471b-a6d0-923010f78f24)

Por último, hacemos un send, y obtenemos un 200 como respuesta.

![5 1](https://github.com/user-attachments/assets/479b2785-5f69-4805-b396-7cc81bfcf6fd)
