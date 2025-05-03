# 🧪 QA Automatizada - Proyecto Urban Grocers App

Este repositorio contiene pruebas automatizadas para la funcionalidad de creación de kits de productos en la aplicación **Urban Grocers**

## 📁 Estructura del proyecto

qa-project-Urban-Grocers-app-es/
│
├── configuration.py # Configuración general del entorno (URL base, etc.)
├── create_kit_name_kit_test.py # Archivo principal de pruebas de creación de kits
├── data.py # Cuerpos de solicitud, headers y datos auxiliares
├── sender_stand_request.py # Funciones para enviar solicitudes HTTP a la API
├── README.md # Este archivo
└── .gitignore # Exclusiones de Git

## ✅ Funcionalidad probada

Se prueba la **creación de un kit de productos**, evaluando distintos casos para el campo `"name"`:

| # | Descripción | Resultado esperado     |
|---|-------------|------------------------|
| 1 | Nombre válido de 1 caracter | 201                    |
| 2 | Nombre de 511 caracteres | 201                    |
| 3 | Nombre de 512 caracteres | 400                    |
| 4 | Nombre de 513 caracteres | 400                    |
| 5 | Caracteres especiales | 201                    |
| 6 | Espacios en el nombre | 201                    |
| 7 | Números como string | 201                    |
| 8 | Falta el parámetro `"name"` | 400                    |
| 9 | `"name"` con tipo incorrecto (número) | ❌ 201 (bug encontrado) |

## 🧰 Tecnologías utilizadas

- Python 3.11+
- Pytest
- Requests

▶️ Pasos para ejecutar las pruebas
Sigue estos pasos para ejecutar correctamente las pruebas automatizadas del proyecto:

1. Clona el repositorio (si aún no lo tienes):
git clone https://github.com/tu_usuario/qa-project-Urban-Grocers-app-es.git
cd qa-project-Urban-Grocers-app-es
2. Instala las dependencias necesarias (si aún no las tienes):
pip install pytest requests
3. Ejecuta todas las pruebas del archivo de test:
pytest create_kit_name_kit_test.py
4. Ejecuta una prueba específica:
pytest create_kit_name_kit_test.py::nombre_de_la_funcion_de_prueba
Ejemplo: pytest create_kit_name_kit_test.py::test_create_kit_with_empty_name

⚠️ Requisitos previos

-Asegúrate de que el servidor de Urban Grocers (contenedor) esté activo antes de ejecutar las pruebas.

-Verifica que la URL base esté correctamente configurada en el archivo configuration.py.

-Los archivos sender_stand_request.py y data.py deben estar presentes y correctamente importados en los tests.

✍️ Autor =
Proyecto desarrollado por Katherine Torres Rodríguez.
