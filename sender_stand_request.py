import requests
from data import user_info, card_id_1, auth_token
from configuration import URL_SERVICE, CREATE_USER_PATH, KITS_PATH

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

