## Sistema de Registro de Infracciones de Transito (SRIT)

Endpoints del servivio

> [!IMPORTANT]
> Para gestionar servicios es requerido el siguiente Token Bearer. de utilizar Postman ingresarlo en authenticación Header 

## TOKEN Requerido para realizar gestiones

```bash
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3MTM3MjE1NjIsImV4cCI6MTcyOTI3MzU2MiwiaWQiOjAsInVzZXJuYW1lciI6IlJheSIsImZ1bGxuYW1lIjoiUmF5YW4gUmF5Iiwicm9sZXMiOlsiYWRtaW4iLCJlZGl0Il19.QkyZHGBa2OdwbhEQ2eMzWjRyH0iHJZ-X5MkxlAMQ4og
```
Registrando el token en la interface web

![image](https://github.com/jmcmaster77/SRIT/assets/85424450/41d4d370-9b10-4270-bc1d-45654e8a0258)

![image](https://github.com/jmcmaster77/SRIT/assets/85424450/af172f86-fcc9-4d86-8a3d-9897ff0171fc)

> [!NOTE]
> Usuario de prueba para generar un nuevo token. es Ray y la clave seria ray12345. de realizar la peticion por postman se podrian realizar con el siguiente json.

```json
{
	"id": 0,
    "username": "Ray",
    "password": "ray12345"
}
```

## Consulta de Personas

```bash
curl --request GET \
  --url http://localhost:5000/personas
```

respuesta 

```json
[
  {
    "_id": "66229e47bc3c56e3ecc20f60",
    "idp": 1,
    "fullname": "Jorge Martin",
    "email": "jm@exam.com",
    "registrado": "2024-04-19T12:33:03.969000"
  },
  {
    "_id": "6622ac13ccae731d7fd6a290",
    "idp": 2,
    "fullname": "Eloy Martin",
    "email": "em@edit.com",
    "registrado": "2024-04-22T01:55:38.923000"
  },
  {
    "_id": "6622acc442e08ffe18f94c4c",
    "idp": 3,
    "fullname": "Jorge Martin",
    "email": "jm@exs.com",
    "registrado": "2024-04-19T12:33:03.969000"
  },
]
```
## Registro de Persona

```bash
curl --request POST \
http://localhost:5000/personas
```

respuesta 

```json
{
  "mensajes":"Persona Registrada"
}
```

> [!NOTE]
> la base de datos requiere un usuario jm y el pass es 15332, con el cual de requerir hacer una conexion con una instancia distinta de mongodb las variables de entorno seria

```bash
MONGO_URI = 'mongodb://localhost:27017/'
```
o modificar las variables de entorno el el archo .env

> [!CAUTION]
> Validaciones a tener en cuenta

Se debe registrar una persona el correo electrónico no debe ser igual al de otra persona.
Para registrar un vehículo de indicar el idp (id de persona registrada).
Para poder registrar una infracción se requiere de placa de vehículo y el idof (id de oficial).
Para consultar una infracción se debe colocar el email de la persona registrada.

## Consulta de Infraccion utilizando un correo de una persona registrada.

![image](https://github.com/jmcmaster77/SRIT/assets/85424450/bee97d22-d85b-455b-8f67-401b327b7eb0)

## Respuesta

```json
[
  {
    "_id": "662508a3b24c39d9043f17ef",
    "fullname": "Ailyn Perez",
    "email": "aperez@gmail.com",
    "idp": 4,
    "placa": "AU5GT04",
    "marca": "Chevrolet",
    "multa": 8.5,
    "comentario": "esto es un comentario",
    "pagado": false
  },
  {
    "_id": "662508a3b24c39d9043f17ef",
    "fullname": "Ailyn Perez",
    "email": "aperez@gmail.com",
    "idp": 4,
    "placa": "AU5GT04",
    "marca": "Chevrolet",
    "multa": 15,
    "comentario": "Mal estado del vehículo",
    "pagado": false
  }
]
```






