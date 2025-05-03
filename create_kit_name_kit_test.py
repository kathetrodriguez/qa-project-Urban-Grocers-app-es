from configuration import URL_SERVICE, USERS_TABLE_PATH
from sender_stand_request import create_user, post_new_client_kit
from data import auth_token, kit_body, headers, kit_body_name_limit_511, kit_body_name_no_limit_512
import requests
import pytest


def positive_assert(kit_body):
    response = post_new_client_kit(kit_body)

    # Verificamos que el código de respuesta sea 201
    assert response.status_code == 201, f"Esperado 201 pero se obtuvo {response.status_code}"

    # Verificamos que el campo "name" en la respuesta coincida con el enviado
    response_json = response.json()
    assert response_json["name"] == kit_body["name"], (
        f'El valor de "name" en la respuesta ({response_json["name"]}) '
        f'no coincide con el enviado ({kit_body["name"]})'
    )

def negative_assert(kit_body):
    response = post_new_client_kit(kit_body)
    print("Respuesta del servidor:", response.status_code, response.text)
    assert response.status_code == 400, f"Esperado 400 pero se obtuvo {response.status_code}"

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

# Prueba 6 	    Se permiten espacios: kit_body = { "name": " A Aaa " }

kit_body_with_spaces = {"name": " A Aaa "}

def test_create_kit_name_with_spaces():
    # Enviamos un nombre con espacios
    response = post_new_client_kit(kit_body_with_spaces)

    # Verificamos que la respuesta sea 201 (creado con éxito)
    assert response.status_code == 201, f"Esperado 201 pero se obtuvo {response.status_code}"
    response_json = response.json()
    assert response_json["name"] == kit_body_with_spaces["name"], "El nombre en la respuesta no coincide con el enviado"

# Prueba 7      Se permiten números: kit_body = { "name": "123" }

kit_body_name_numbers = {
    "name": "123"
}
def test_create_kit_name_with_numbers():
    positive_assert(kit_body_name_numbers)

# Prueba 8 	El parámetro no se pasa en la solicitud: kit_body = { }

def test_create_kit_without_name_parameter():
    kit_body = {}  # No se incluye el parámetro "name"
    negative_assert(kit_body)

# Prueba 9: 	Se ha pasado un tipo de parámetro diferente (número): kit_body = { "name": 123 }

def test_create_kit_with_number_as_name():
    kit_body = {
        "name": 123  # tipo de dato incorrecto (entero en vez de string)
    }
    negative_assert(kit_body)