from configuration import URL_SERVICE, USERS_TABLE_PATH
from sender_stand_request import create_user, post_new_client_kit
from data import auth_token, kit_body, headers, kit_body_name_limit_511, kit_body_name_no_limit_512
import requests
import pytest


def test_user_authenticated_successfully():
    # Construye la URL completa para acceder a la tabla de usuarios
    url = URL_SERVICE + USERS_TABLE_PATH
    # Copia los headers base y añade el token de autenticación
    auth_headers = headers.copy()
    auth_headers["Authorization"] = f"Bearer {auth_token}"
    # Envía una solicitud GET autenticada para consultar la tabla de usuarios
    response = requests.get(url, headers=auth_headers)
    # Verifica que la respuesta tenga un código de estado HTTP 200 (OK)
    assert response.status_code == 200, f"Expected 200 but got {response.status_code}"
    # Extrae el contenido de la respuesta como texto (la tabla CSV de usuarios)
    content = response.text
    # Verifica que el token esperado esté presente en la tabla de usuarios
    assert auth_token in content, "authToken no encontrado en la respuesta"
    #imprime un mensaje indicando que la prueba fue exitosa
    print("Prueba positiva: el usuario con el token fue encontrado en la tabla.")


#Lista de comprobación de pruebas

# Prueba #1 El número permitido de caracteres (1): kit_body = { "name": "a"}
def test_create_kit_name_with_1_character():
    # # Cuerpo con "name" de 1 carácter
    kit_body = {"name": "a"}
    # Envía la solicitud
    response = post_new_client_kit(kit_body)
    # Verifica que el estado sea 201 (creado)
    assert response.status_code == 201, f"Expected 201 but got {response.status_code}"
    # Verifica que el nombre en la respuesta sea igual al enviado
    assert response.json()["name"] == kit_body["name"], "El campo 'name' no coincide"

# Prueba #2 El número permitido de caracteres maximo (511)
def test_create_kit_name_with_511_characters():
    # Enviamos la solicitud con un nombre de 511 caracteres
    response = post_new_client_kit(kit_body_name_limit_511)

    # Verificamos que el código de estado sea 201 (creado)
    assert response.status_code == 201, f"Esperado 201 pero se obtuvo {response.status_code}"

    # Comprobamos que el nombre en la respuesta sea igual al enviado
    assert response.json()["name"] == kit_body_name_limit_511["name"], "El campo 'name' no coincide"

# Prueba #3 	El número de caracteres es menor que la cantidad permitida (0): kit_body = { "name": "" }
def test_create_kit_name_with_0_characters():
    # Enviamos la solicitud con un nombre vacío
    kit_body = {"name": ""}
    response = post_new_client_kit(kit_body)

    # Verificamos que el código de estado sea 400 (error por nombre inválido)
    assert response.status_code == 400, f"Esperado 400 pero se obtuvo {response.status_code}"

# Prueba 4  	El número de caracteres es mayor que la cantidad permitida (512)
def test_create_kit_name_with_more_than_512_characters():
    # Enviamos el cuerpo con más de 512 caracteres
    response = post_new_client_kit(kit_body_name_no_limit_512)

    # Verificamos que la respuesta sea 400 (error por exceso de caracteres)
    assert response.status_code == 400, f"Esperado 400 pero se obtuvo {response.status_code}"

# Prueba 5      Se permiten caracteres especiales: kit_body = { "name": ""№%@"," }
def test_create_kit_name_with_special_characters():
    # Cuerpo con caracteres especiales
    kit_body = {"name": "№%@"}
    response = post_new_client_kit(kit_body)

    # Verificamos que la respuesta sea 201 (éxito)
    assert response.status_code == 201, f"Esperado 201 pero se obtuvo {response.status_code}"
    assert response.json()["name"] == kit_body["name"], "El campo 'name' no coincide"
    