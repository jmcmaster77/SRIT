Sistema de Registro de Infracciones de Transito (SRIT)

Api escrita en python, fastAPI, mongoDB 

con esta add se puede registrar usuarios y obtener un JWT para acceder a las distintas api para registrar personas, vehiculos, oficiaes y por ultimo infracciones de Transito 

estas se pueden acceder desde la interface generada con FastAPI http://localhost:5000/docs#/

Primero, crear un entorno virtual:

python -m virtualenv venv

Para instalar los paquetes necesarios:

pip install -r requirements.txt

python src\main.py




![image](https://github.com/jmcmaster77/SRIT/assets/85424450/66dff32f-c82c-4e1c-ac09-c62fd6c36e5b)

![image](https://github.com/jmcmaster77/SRIT/assets/85424450/b5ea8419-840f-4d4f-9d2a-233535bc434a)

pueden descargar el proyecto modificar .env para editar la ip y apuntar al contenedor o servidor de mongo donde hagan la restauracion de la base de datos. SRIT el dump srit_dev.db esta disponible en los archivos 

usuario de la basede datos mongo es -u jm -p 15332


el Docker File esta preparado para realizar un  build de un  contenedor con una imagen de alpine 

utilizar el siguiente comando en la carpeta donde hagan el pull de la app api 
docker build -t SRIT . 

![image](https://github.com/jmcmaster77/SRIT/assets/85424450/05f9508c-3b4f-46e4-8075-21f6da5ccf87)

JWT de prueba 

token user
Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3MTM3MjE1NjIsImV4cCI6MTcyOTI3MzU2MiwiaWQiOjAsInVzZXJuYW1lciI6IlJheSIsImZ1bGxuYW1lIjoiUmF5YW4gUmF5Iiwicm9sZXMiOlsiYWRtaW4iLCJlZGl0Il19.QkyZHGBa2OdwbhEQ2eMzWjRyH0iHJZ-X5MkxlAMQ4og

token oficial 
Bearer
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3MTM3ODMzNjAsImV4cCI6MTcyOTMzNTM2MCwiaWQiOjEsInVzZXJuYW1lciI6InBpY2FwaWVkcmEiLCJmdWxsbmFtZSI6IlBlZHJvIFBpY2FwaWVkcmEiLCJyb2xlcyI6WyJhZG1pbiIsImVkaXQiXX0.fasWb6Smz1zTw4Q-zo0MPdippGgSEKlJOH21KqD664A

![image](https://github.com/jmcmaster77/SRIT/assets/85424450/7674527a-c664-4958-bcfa-95c75a1776ea)

