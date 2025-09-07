🧪 **Proyecto de pruebas automatizadas – Urban Grocers App**

Este proyecto contiene un conjunto de pruebas automáticas para verificar que la aplicación Urban Grocers funcione correctamente cuando los usuarios crean un kit de productos (una especie de paquete con varios artículos).

**🎯 Objetivos**

Objetivo general:
Asegurar la calidad de la funcionalidad de creación de kits en la aplicación Urban Grocers mediante pruebas automatizadas que validen diferentes escenarios de uso.

Objetivos específicos:

Validar que el sistema acepte correctamente nombres de kits dentro de los límites permitidos.

Detectar errores cuando el campo name no cumple con el formato esperado (vacío, demasiado largo, tipo de dato incorrecto, etc.).

Generar un proceso automatizado que permita ejecutar las pruebas de forma rápida y repetible, facilitando la detección de bugs.

**📁 ¿Qué hay en el proyecto?**

Dentro de la carpeta principal encontrarás:

configuration.py → Datos de configuración, como la dirección de la aplicación.

create_kit_name_kit_test.py → El archivo que contiene las pruebas principales.

data.py → Información extra que se usa en las pruebas (ejemplo: encabezados, textos).

sender_stand_request.py → Funciones que se encargan de enviar las solicitudes a la aplicación.

README.md → Explicación del proyecto (este archivo).

.gitignore → Archivos que no se guardan en el repositorio.

**✅ ¿Qué estamos probando?**

Se revisa que el campo “nombre del kit” funcione bien en diferentes situaciones.
Por ejemplo:

Nombre con 1 solo carácter → debería funcionar.

Nombre con 511 caracteres → debería funcionar.

Nombre con 512 o más caracteres → debería dar error.

Nombre con símbolos o caracteres especiales → debería funcionar.

Nombre solo con espacios → debería funcionar.

Nombre con números → debería funcionar.

Cuando falta el nombre → debería dar error.

Cuando el nombre tiene un tipo incorrecto (número en lugar de texto) → debería dar error, pero aquí se encontró un bug (la aplicación lo acepta como válido).

**🛠️ Tecnologías utilizadas**

Python 3.11+

Pytest (herramienta para correr las pruebas)

Requests (para comunicarse con la aplicación)

**▶️ ¿Cómo se ejecutan las pruebas?**

Descargar el proyecto.

Instalar las dependencias necesarias.

Asegurarse de que el servidor de Urban Grocers esté encendido.

Ejecutar las pruebas con un comando sencillo en la terminal.

**✍️ Autor**

Proyecto desarrollado por Katherine Torres Rodríguez.
