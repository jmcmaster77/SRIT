# Project name
## Sistema de Registro de Infracciones de Transito (SRIT)

## Version 

Versión en desarrollo v.0.5

## Description

Api escrita en python, fastAPI con conexion a una base de datos alojada en mongoDB esta api brinda los siguientes grupos de endpoints en los que se gestiona usuarios, generar token, personas, vehiculos, oficiales y infracciones.

## Requerimientos e instalación 

Se requiere docker para ejecutar esta api.

## Build 

```bash
docker-compose up -d
```

.[!NOTE].
Esta api está configurada con el puerto 5000 para la api y el puerto 27017 para el servidor de mongodb.

.[!WARNING].
Si tienes un servidor de mongodb activo para evitar conflictos detén el servicio.

luego

```bash
docker-compose up
```

### Los enpoints se encuentran publicados en el siguiente link 

http://localhost:5000/docs

.[!WARNING]. verificar que el contenedor está en ejecución

### Documentacion adicional 

En el siguiente apartado, se puede ver la documentación mas detallasa de la api.

[Documentación detallada](API.md)
