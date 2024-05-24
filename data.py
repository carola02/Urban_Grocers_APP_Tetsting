headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + "authToken"
}

headers_for_kit = {
    "Content-Type": "application/json",
    "Authorization": "Bearer token"
}

user_body = {
    "firstName": "Carolina",
    "phone": "+11234567890",
    "address": "742 Evergreen Terrace, Springfield"}


product_ids = {
    "ids": [1, 2, 3]}

# clase de kit_body -> dentor de la clase los difentes

kit_body = {
       "name": "Mi conjunto de prueba primer intento",
       "card": {
           "id": 1,
           "name": "Para la situación"},
       "productsList": [],
       "id": 7,
       "productsCount": 0
}

# Ver adentro del diccionario
# print(kit_body["card"]["name"])
