# Ampliación de Base de Datos - Big Data

La práctica trataba de crear archivos de tipo map reduce para analizar los datos que había en un archivo aparte, los objetivos principales eran: descartar las líneas que no fueran válidas porque los datos no fueran suficientes o inválidos y realizar las búsquedas de tal manera que pudieran escalar si los datos fueran más grandes no desbordasen la memoria.

Los datos estaban prsentados en un log con el siguente formato.
```
in24.inetnebr.com;-;-;1995-08-01 00:00:01;GET;/shuttle/missions/sts-68/news/sts-68-mcc-05.txt;HTTP/1.0;200;1839
uplherc.upl.com ;-;-;1995-08-01 00:00:07;GET;/;HTTP/1.0;304;0
uplherc.upl.com;-;-;1995-08-01 00:00:08;GET;/images/ksclogo-medium.gif;HTTP/1.0;304;0
```

## Busquedas
1. Número de peticiones de tipo GET
2. Número de peticiones por tipo (GET, POST, PUT, etc.)
3. Media/porcentaje de peticiones por tipo (GET, POST, PUT, etc.)
4. Tipos de respuesta por familia (2XX, 3XX, 4XX y 5XX) por tipo de petición (GET, POST,
PUT, etc.)
5. Tipos de archivo (.gif, .html, etc.) no encontrados (404) en un hora determinada.
6. Incremento/decremento por hora (en porcentaje) del tráfico en bytes (último dato).
7. Top tres dominios que más tráfico tiene en bytes (último dato).8. Top tres tipos de archivos (.gif, .html, etc.) que más tráfico produce en bytes (último dato)
por dominio.
9. Balance de tráfico en bytes (último dato) por dominio. Descargas (GET) menos subidas
(POST)
