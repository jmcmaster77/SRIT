# Project name
Sistema de Registro de Infracciones de Transito (SRIT)

# Version 

Versión en desarrollo v.0.1

## Description

Api escrita en python, fastAPI con conexion a una base de datos alojada en mongoDB

## Requirements and Installation

Se pueden ver en el archivo requirements.txt.

## Ejecutar la app

```bash
docker-compose build
```

luego

```bash
docker-compose up
```

## Ejecutar ingresar a la siguiente url

http://localhost:5000/docs

# token de prueba 

token user
Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3MTM3MjE1NjIsImV4cCI6MTcyOTI3MzU2MiwiaWQiOjAsInVzZXJuYW1lciI6IlJheSIsImZ1bGxuYW1lIjoiUmF5YW4gUmF5Iiwicm9sZXMiOlsiYWRtaW4iLCJlZGl0Il19.QkyZHGBa2OdwbhEQ2eMzWjRyH0iHJZ-X5MkxlAMQ4og

con esta api brinda los siguientes grupos de endpoints en los que se gestiona usuarios, generar token, personas, vehiculos, oficiales y infracciones.

estas se pueden acceder desde la interface generada con FastAPI http://localhost:5000/docs

pueden descargar el proyecto modificar .env para editar la ip y apuntar al contenedor o servidor de mongo donde hagan la restauracion de la base de datos. SRIT el dump srit_dev.db esta disponible en los archivos 

usuario de la basede datos mongo es -u jm -p 15332

el Docker File esta preparado para realizar un  build de un  contenedor con una imagen de alpine 

utilizar el siguiente comando en la carpeta donde hagan el pull de la app api 
docker build -t SRIT . 

JWT de prueba 

token user
Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3MTM3MjE1NjIsImV4cCI6MTcyOTI3MzU2MiwiaWQiOjAsInVzZXJuYW1lciI6IlJheSIsImZ1bGxuYW1lIjoiUmF5YW4gUmF5Iiwicm9sZXMiOlsiYWRtaW4iLCJlZGl0Il19.QkyZHGBa2OdwbhEQ2eMzWjRyH0iHJZ-X5MkxlAMQ4og

token oficial 
Bearer
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3MTM3ODMzNjAsImV4cCI6MTcyOTMzNTM2MCwiaWQiOjEsInVzZXJuYW1lciI6InBpY2FwaWVkcmEiLCJmdWxsbmFtZSI6IlBlZHJvIFBpY2FwaWVkcmEiLCJyb2xlcyI6WyJhZG1pbiIsImVkaXQiXX0.fasWb6Smz1zTw4Q-zo0MPdippGgSEKlJOH21KqD664A

![image](https://github.com/jmcmaster77/SRIT/assets/85424450/7674527a-c664-4958-bcfa-95c75a1776ea)

