🧪 Proyecto de Pruebas Automatizadas – Urban Grocers App

Este repositorio contiene pruebas automáticas para la aplicación Urban Grocers, enfocadas en la funcionalidad de creación de kits de productos (paquetes de artículos).

El objetivo es comprobar que la aplicación responda correctamente cuando se intenta crear un kit con diferentes tipos de nombres.

📁 Estructura del proyecto
📁 qa-project-Urban-Grocers-app-es/
├── ⚙️ configuration.py        # Configuración general (ejemplo: URL base)
├── 🧪 create_kit_name_kit_test.py # Pruebas principales de creación de kits
├── 📄 data.py                  # Datos de apoyo (encabezados, cuerpos de solicitud, etc.)
├── 📤 sender_stand_request.py  # Funciones para enviar solicitudes a la API
├── 📝 README.md                # Este archivo
└── 🚫 .gitignore               # Archivos excluidos del repositorio


✅ Funcionalidad probada

Se validan distintos casos para el campo "name" del kit:

#	Descripción	Resultado esperado
1	Nombre válido de 1 caracter	201
2	Nombre de 511 caracteres	201
3	Nombre de 512 caracteres	400
4	Nombre de 513 caracteres	400
5	Uso de caracteres especiales	201
6	Nombre con espacios	201
7	Nombre compuesto solo por números	201
8	Falta el parámetro "name"	400
9	"name" con tipo incorrecto (número)	❌ 201 (bug encontrado)
🛠️ Tecnologías utilizadas

Python 3.11+

Pytest

Requests

▶️ Ejecución de las pruebas

Clonar el repositorio:

git clone https://github.com/tu_usuario/qa-project-Urban-Grocers-app-es.git
cd qa-project-Urban-Grocers-app-es


Instalar dependencias:

pip install pytest requests


Ejecutar todas las pruebas:

pytest create_kit_name_kit_test.py


Ejecutar una prueba específica:

pytest create_kit_name_kit_test.py::nombre_de_la_funcion

⚠️ Requisitos previos

Tener el servidor de Urban Grocers encendido.

Verificar que la URL base esté configurada en configuration.py.

Contar con los archivos sender_stand_request.py y data.py en el proyecto.

✍️ Autor

Proyecto desarrollado por Katherine Torres Rodríguez.

-Verifica que la URL base esté correctamente configurada en el archivo configuration.py.

-Los archivos sender_stand_request.py y data.py deben estar presentes y correctamente importados en los tests.

✍️ Autor =
Proyecto desarrollado por Katherine Torres Rodríguez.
