## Sistema de Registro de Infracciones de Transito (SRIT)

Endpoints del servivio

> [!IMPORTANT]
> Para gestionar servicios es requerido el siguiente Token Bearer. de utilizar Postman ingresarlo en authenticación Header 

## TOKEN Requerido para realizar gestiones

```bash
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3MTM3MjE1NjIsImV4cCI6MTcyOTI3MzU2MiwiaWQiOjAsInVzZXJuYW1lciI6IlJheSIsImZ1bGxuYW1lIjoiUmF5YW4gUmF5Iiwicm9sZXMiOlsiYWRtaW4iLCJlZGl0Il19.QkyZHGBa2OdwbhEQ2eMzWjRyH0iHJZ-X5MkxlAMQ4og
```

Registrando el token en la interface web

IMAGE HERE

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