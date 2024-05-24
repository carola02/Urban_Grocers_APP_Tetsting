import configuration
import requests
import data


# Creación de nuevo usuario
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)


response = post_new_user(data.user_body)
print(response.status_code)
print(response.json())


def get_new_user_token():
    new_token = post_new_user(data.user_body)  # new_token:Es el objeto de respuesta HTTP y convierte la respuesta
    # formato JSON en  diccionario Python
    response_json = new_token.json()  # response_json: Es el diccionario que contiene los datos de la respuesta JSON.
    auth_token_user = response_json.get("Authorization")  # response_json.get(""): Accede al valor de la clave
    # "Authorization" en el diccionario response_json. y la solicitud get solicita lo que contiene el () para acceder
    # al valor de la clave específica en el diccionario.
    return auth_token_user  # devuelve el valor de auth_token a la parte del código que llamó a esta función.


# token = get_new_user_token()
# print(token)
response = post_new_user(data.user_body)
print(response.status_code)
print(response.json())


def post_new_client_kit(token, kit_body):
    headers = data.headers.copy()  # Copia los encabezados desde el acrhivo data.py
    headers["Authorization"] = f"Bearer {token}"  # Agrega el token de autorización al encabezado
    response_new_client = requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                                        json=kit_body,
                                        headers=headers)  # estos son los heraders que se le acaban de indicar
    return response_new_client


token = get_new_user_token()  # Obtiene el token de autorización del usuario creado
response = post_new_client_kit(token, data.kit_body)  # Crea un nuevo kit utilizando el token que se acaba de llamar
# y el cuerpo importado del archivo data
print(response.status_code)
print(response.json())
