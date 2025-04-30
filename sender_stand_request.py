import requests
from configuration import URL_SERVICE

def create_user():
    user_data = {
    "firstName": "Angela",
    "phone": "+573186542187",
    "address": "cra 34 n52 - 21"
    }
    response = requests.post(f"{URL_SERVICE}/users/",json=user_data)
    response.raise_for_status()
    return response.json()["authToken"]

def create_kit(auth_token, kit_data):
    headers = {
        "Authorization": f"Bearer {auth_token}"
    }

    response = requests.post(
        url=f"{URL_SERVICE}/kits",
        json=kit_data,
        headers=headers
    )

    response.raise_for_status()
    return response.json()

