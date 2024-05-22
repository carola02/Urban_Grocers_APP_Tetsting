# Proyecto Urban Grocers 
CONTENIDO DEL ARCHIVO README
El objetivo de este proyecto es implementar pruebas automatizadas para la API de Urban Grocers por medio de Pytest. Las pruebas se centran en la funcionalidad de creación de kits, verificando diversos casos en la creación del nombre dle kit 


## Requisitos Previos
- Python 3.8 o superior
- `pip` (el gestor de paquetes de Python)


1. Primer archivo: configuration.py
Este archivo contiene los puntos de conexión del servidor y los endpoint de las APIs que se van a probar durante la ejecución de las pruebas

2. Segundo archivo: data.py
Este archivo centraliza los datos de prueba para las solicitudes que se realizarán desde otros documentos del proyecto como lo son sender_stand_request.py y create_kit_name_kit_test.py

La escritura de datos se realiza en formato Json como está descrito en el APIdocs de la plataforma

3. Tercer archivo: sender_stand_request.py

Este archivo recoge las funciones principales de conexión:

A. post_new_user(body):
* Esta función realiza la conexión al servidor y crea un nuevo usuario.
* El argumento 'body' es el cuerpo de la solicitud que se enviará al servidor para crear un nuevo usuario.
* Se confirma la solicitud de creación del usuario y el cuerpo enviado que debe ser el mismo que se aloja en el archivo Data

B. get_new_user_token():
* Esta función se encarga de crear un nuevo usuario mediante una solicitud HTTP y extraer el token de autorización de la respuesta.

C. post_new_client_kit():
*Esta función recoge el número de token del usuario y el cuerpo del kit para crear un nuevo kit sobre el usuario autenticado 

4. El cuarto archivo: create_kit_name_test.py
Este archivo se dividide en dos partes. Primero, el diseño de funciones bajo el concepto DRY para pruebas positivas y negativas y posteriormente, la creación de 9 pruebas con base en los requerimientos por medio del uso de las funciones para simplificar el código.

La primera función de este archivo es get_kit_body(name): la cual copia el kit body establecido en el archivo data y modifica el parámetro de prueba "name"

La segunda función es positive_assert_201(name): verifica que se pueda crear un kit exitosamente cuando se proporciona un nombre válido. Se asegura de que la respuesta de la API tenga un código de estado 201.

La tercera función negative_assert(name): verifica que la creación de un kit falle cuando se proporciona un nombre inválido o vacío. Se asegura de que la respuesta de la API tenga un código de error 400


Contribuciones
Las contribuciones y comentarios son bienvenidos. Para ello:

Haz un fork de este repositorio.
Crea una nueva rama (git checkout -b feature/nueva-funcionalidad).
Realiza tus cambios y haz commit (git commit -am 'Añadir nueva funcionalidad').
Haz push a la rama (git push origin feature/nueva-funcionalidad).
Abre un Pull Request.
