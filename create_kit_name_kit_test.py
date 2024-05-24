# import configuration
# import requests
import data
import sender_stand_request


# PREPARACIÓN DE PRUEBAS
# Primero get_kit_body devolviendo correctamente el cuerpo del kit con un nombre vacío:
def get_kit_body(name):  # esta función cambia los valores en el parámetro "name"
    kit_body = data.kit_body.copy()  # el diccionario que contiene el cuerpo de solicitud se copia del archivo "data"
    # (datos) para conservar los datos del diccionario de origen
    kit_body["name"] = name  # Actualiza el nombre del kit con el parámetro proporcionado
    return kit_body


def positive_assert_201(name):
    kit_body = get_kit_body(name)  # El cuerpo de la solicitud actualizada se guarda en la variable user_body
    token = sender_stand_request.get_new_user_token()  # Obtiene el token de autorización del usuario
    kit_response = sender_stand_request.post_new_client_kit(token, kit_body)  # Envía la solicitud para crear un nuevo
    # kit con el token del usuario creado
    # usuario/a se guarda en la variable user_response
    assert kit_response.status_code == 201  # Comprueba si el código de estado es 201


def negative_assert(name):
    token = sender_stand_request.get_new_user_token()  # Obtiene el token de autorización del usuario
    kit_body = get_kit_body(name)  # Utiliza el nombre proporcionado para obtener el cuerpo del kit
    kit_negative_response = sender_stand_request.post_new_client_kit(token, kit_body)
    assert kit_negative_response.status_code == 400  # Verifica que la solicitud no se haya realizado con éxito


# Código respuesta: 201 Campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud
# El número permitido de caracteres (1): kit_body = { "name": "a"}
def test1_kit_body_name_1_character_name_get_success_response():
    positive_assert_201("a")


# Código de respuesta: 201 Campo "name" en el cuerpo de la respuesta coincide con campo "name" en el cuerpo de solicitud
# El num ermitido de caracteres(511): kit_body = { "name":"El valor de prueba para esta comprobación será inferior a"}
def test2_kit_body_max_character_length_name_get_success_response():
    positive_assert_201("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda\
    bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd\
    abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab\
    cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda\
    bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")


# @pytest.mark.xfail(reason="Known issue: API permite la creación de un kit con nombre vacío. Confirmado de forma
# manual por medio de Postman")
# Código respuesta: 201 El campo "name" en el cuerpo de la respuesta coincide con el campo "name" en cuerpo de solicitud
def test3_kit_body_zero_character_length_name_get_error_response():
    negative_assert("")


# El número de caracteres es mayor que la cantidad permitida (512): kit_body = { "name":"El valor de prueba para esta
# comprobación será inferior a” }
# Código de respuesta: 400
def test4_kit_body_max_character_length_plus_1_name_get_error_response():
    negative_assert("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab\
    cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda\
    bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd\
    abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc\
    dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")


# Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo
# de la solicitud
# Se permiten caracteres especiales: kit_body = { "name": ""№%@"," }
def test5_kit_body_special_character_name_get_success_response():
    positive_assert_201("№%@")


# Se permiten espacios: kit_body = { "name": " A Aaa " }
# Código de respuesta: 201 Campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo la solicitud
def test6_kit_body_spaces_in_name_field_name_get_success_response():
    positive_assert_201(" A Aaa ")


# Se permiten números: kit_body = { "name": "123" }
# Código de respuesta: 201 Campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo la solicitud
def test7_kit_body_numbers_in_name_field_get_success_response():
    positive_assert_201("123")


# El parámetro no se pasa en la solicitud: kit_body = { }
# Código de respuesta: 400
def test8_kit_body_missing_parameter_name_get_error_response():
    negative_assert({})


# Se ha pasado un tipo de parámetro diferente (número): kit_body = { "name": 123 }
# Código de respuesta: 400
def test9_kit_body_different_parameter_type_name_get_error_response():
    negative_assert(123)
