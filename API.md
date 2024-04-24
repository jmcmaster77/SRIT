# Activity Service

Endpoints del microservicio de actividades.


## Obtener las actividades

```bash
curl --request GET \
  --url http://0.0.0.0:8000/users/b9e605ee-4cca-400e-99c5-ae24abca97d5/projects/016fe969-4d2f-43f9-81b4-1bdcebd975e4/activities/
```

respuesta 

```json
[
  {
    "id": "afcc1b39-8887-4027-977d-5b1cbff2e533",
    "user": "b9e605ee-4cca-400e-99c5-ae24abca97d5",
    "project": "016fe969-4d2f-43f9-81b4-1bdcebd975e4",
    "rule": "6e10b138-9899-43cf-8a62-d6119456aa82",
    "payment": "edf6a8f3-3081-414e-9b2f-4b6fa32eba2e",
    "project_name": "Meta de prueba",
    "amount": "1000.00",
    "title": "Title",
    "message": "Message",
    "footer": "Footer",
    "rule_name": "Rule Name",
    "rule_icon": "Icon",
    "created_at": "2022-01-27T00:00:00-06:00"
  }
]
```
## Crear una actividad

```bash
curl --request POST \
  --url http://0.0.0.0:8000/users/b9e605ee-4cca-400e-99c5-ae24abca97d5/projects/016fe969-4d2f-43f9-81b4-1bdcebd975e4/activities/ \
  --header 'content-type: application/json' \
  --data '{"rule": "6e10b138-9899-43cf-8a62-d6119456aa82","payment": "edf6a8f3-3081-414e-9b2f-4b6fa32eba2e","project_name": "Meta de prueba","amount" : 1000,"title": "Title","message": "Message","footer": "Footer","rule_name": "Rule Name","rule_icon": "Icon", "activity_type": "E"}'
```

respuesta 

```json
{
   "user":"b9e605ee-4cca-400e-99c5-ae24abca97d5",
   "project":"016fe969-4d2f-43f9-81b4-1bdcebd975e4",
   "project_name":"Nombre meta",
   "rule":null,
   "rule_name":null,
   "payment":null,
   "amount":8000.0,
   "title":"Probando creacion de actividades",
   "message":"Probando creacion de actividades desde crear meta",
   "footer":"footer",
   "rule_icon":"icon",
   "activity_type":{
      "code":"E",
      "value":"Event"
   },
   "id":"fc57e25a-5612-4ee6-b66c-d63aaa536814",
   "created_at":"2022-04-03T04:12:05.793310"
}
```

## Ver el detalle de una actividad

```bash
curl --request GET \
  --url http://127.0.0.1/activity-service/users/b9e605ee-4cca-400e-99c5-ae24abca97d5/projects/016fe969-4d2f-43f9-81b4-1bdcebd975e4/activities/afcc1b39-8887-4027-977d-5b1cbff2e533/
```

respuesta 

```json
{
  "id": "afcc1b39-8887-4027-977d-5b1cbff2e533",
  "user": "b9e605ee-4cca-400e-99c5-ae24abca97d5",
  "project": "016fe969-4d2f-43f9-81b4-1bdcebd975e4",
  "rule": "6e10b138-9899-43cf-8a62-d6119456aa82",
  "payment": "edf6a8f3-3081-414e-9b2f-4b6fa32eba2e",
  "project_name": "Meta de prueba",
  "amount": "1000.00",
  "title": "Title",
  "message": "Message",
  "footer": "Footer",
  "rule_name": "Rule Name",
  "rule_icon": "Icon",
  "created_at": "2022-01-27T00:00:00-06:00"
}
```

# Actualizar parcialmente la actividad. Forma 1

```bash
curl --request PATCH \
  --url http://127.0.0.1/activity-service/users/b9e605ee-4cca-400e-99c5-ae24abca97d5/projects/016fe969-4d2f-43f9-81b4-1bdcebd975e4/activities/afcc1b39-8887-4027-977d-5b1cbff2e533/ \
  --header 'content-type: application/json' \
  --data '{"rule_name": "Rule Name PATCH"}'
```

respuesta 

```json
{
  "id": "afcc1b39-8887-4027-977d-5b1cbff2e533",
  "user": "b9e605ee-4cca-400e-99c5-ae24abca97d5",
  "project": "016fe969-4d2f-43f9-81b4-1bdcebd975e4",
  "rule": "6e10b138-9899-43cf-8a62-d6119456aa82",
  "payment": "edf6a8f3-3081-414e-9b2f-4b6fa32eba2e",
  "project_name": "Meta de prueba",
  "amount": "1000.00",
  "title": "Title",
  "message": "Message",
  "footer": "Footer",
  "rule_name": "Rule Name PATCH",
  "rule_icon": "Icon",
  "created_at": "2022-01-27T15:44:58.515852-06:00"
}
```

# Actualizar parcialmente la actividad. Forma 2

```bash
curl --request PUT \
  --url http://127.0.0.1/activity-service/users/b9e605ee-4cca-400e-99c5-ae24abca97d5/projects/016fe969-4d2f-43f9-81b4-1bdcebd975e4/activities/afcc1b39-8887-4027-977d-5b1cbff2e533/ \
  --header 'content-type: application/json' \
  --data '{"user": "b9e605ee-4cca-400e-99c5-ae24abca97d5","project": "016fe969-4d2f-43f9-81b4-1bdcebd975e4","rule": "6e10b138-9899-43cf-8a62-d6119456aa82","payment": "edf6a8f3-3081-414e-9b2f-4b6fa32eba2e","amount" : 10000,"title": "Title Put","message": "Message Put","footer": "Footer Put"}'
```
respuesta

```json
  {
  "id": "afcc1b39-8887-4027-977d-5b1cbff2e533",
  "user": "b9e605ee-4cca-400e-99c5-ae24abca97d5",
  "project": "016fe969-4d2f-43f9-81b4-1bdcebd975e4",
  "rule": "6e10b138-9899-43cf-8a62-d6119456aa82",
  "payment": "edf6a8f3-3081-414e-9b2f-4b6fa32eba2e",
  "project_name": "Meta de prueba",
  "amount": "10000.00",
  "title": "Title Put",
  "message": "Message Put",
  "footer": "Footer Put",
  "rule_name": "Rule Name PATCH",
  "rule_icon": "Icon",
  "created_at": "2022-01-27T15:52:54.459960-06:00"
}
```