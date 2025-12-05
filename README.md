# Proyecto final-automation-testing

## Propósito del Proyecto

Automatizar flujos básicos de navegación web en la página **www.saucedemo.com**, interactuando con elementos web y validando estados, utilizando una arquitectura Page Object Model (POM).

Automatizar pruebas para la API REST pública https://jsonplaceholder.typicode.com/, cubriendo los métodos fundamentales GET, POST y DELETE.

---

## Tecnologías Utilizadas

Para el desarrollo y ejecución de este proyecto se utilizaron las siguientes herramientas y tecnologías:

| Tecnología | Rol |
| **Python** | Lenguaje de programación principal. |
| **Pytest** | Framework para la estructura, descubrimiento y ejecución de pruebas. |
| **Selenium WebDriver** | Herramienta para la automatización de la interacción con el navegador web. |
| **Git** & **GitHub** | Control de versiones y repositorio de código. |
| **Request** | Librería de Python para realizar llamadas y pruebas a APIs HTTP. |
| **pytest-html** | Plugin para generar reportes HTML detallados de las ejecuciones. |

# Estructura del proyecto
El código se organiza en 2 carpetas principales:
| **Pruebas API** | Donde se encuentra un archivo unico con los tests para 3 tipos de peticiones.
 |**Pruebas UI** | Se divide en 4 carpetas: archivos de datos, paginas de la web a probar, tests y módulos auxiliares.

Dentro de cada archivo se encuentran algunos comentarios descriptivos.

---

## Instalación de Dependencias

Para configurar y ejecutar el proyecto, se deben seguir los siguientes pasos:

1.  **Creación del repositorio:**
    Una vez que se tiene **Git** instalado, se configura desde la consola de la siguiente manera:

    ```
    git config --global user.name "Tu Nombre"
    git config --global user.email "tuemail@ejemplo.com"
    ```

    Luego se debe ir a GitHub, crear un nuevo repositorio y vincularlo al repositorio local. A partir de esto se podra seguir el siguente flujo:

    ```
    git init  ->  Por unica vez para iniciar git en el proyecto
    git add .  ->  Agrega cambios al área de preparación
    git commit -m "nombre del cambio"  ->  Crea un snapshot en el historial
    git push  ->  Envía los commits al repositorio remoto (Github).
    ```


2.  **Instalacion de librerias de Python:**
    Una vez que se tiene **Python** instalado, las librerías necesarias se pueden instalar desde la terminal con `pip`:

    ```Para instalar selenium
    pip install selenium
    ```

    ```Para instalar libreria requests y pytest-html 
    pip install requests
    
    pip install pytest-html

    ```

  

3.  **Configuracion el WebDriver:**
    Se instaló el WebDriver necesario para Chrome desde **https://googlechromelabs.github.io/chrome-for-testing/**, donde la versión del driver debe coincidir con la del navegador.
    
    ```Para verificar la instalacion correcta y su version
    chromedriver --version
    ```

---

## Ejecución de las Pruebas

Una vez que las dependencias estén instaladas, se puede ejecutar el conjunto de tests y su reporte respectivo con los siguientes comandos de **Pytest**:

```
cd Pruebas UI      
pytest tests

```
cd Pruebas API      
pytest test_request.py

```
pytest -v --html=reports/ui_api_report.html --self-contained-html
```