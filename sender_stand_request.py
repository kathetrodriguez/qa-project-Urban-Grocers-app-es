import requests
from data import user_info, card_id_1, auth_token, kit_body, headers
from configuration import URL_SERVICE, CREATE_USER_PATH, KITS_PATH, USERS_TABLE_PATH

#Creacion de usuario

def create_user():
    url = URL_SERVICE + CREATE_USER_PATH
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=user_info, headers=headers)
    print("URL:", url)
    print("Status:", response.status_code)
    print("Respuesta:", response.text)

    return response
response = create_user()
try:
    print(response.json())
except ValueError:
    print("Error al decodificar JSON. Respuesta fue:")
    print(response.text)

# Función para consultar la tabla de los usuarios

def get_users_table():
    return requests.get(URL_SERVICE + USERS_TABLE_PATH)


response_user_table = get_users_table()

print(response_user_table.status_code)
print(response_user_table.text)

# Función para crear un kit nuevo
def post_new_client_kit(kit):

    current_headers = headers.copy()
    current_headers["Authorization"] = "Bearer " + response.json()["authToken"]
    return requests.post(URL_SERVICE + KITS_PATH,
                         json= kit,
                         headers= current_headers)

response_kit = post_new_client_kit(kit_body)
print(response_kit.status_code)
print(response_kit.text)