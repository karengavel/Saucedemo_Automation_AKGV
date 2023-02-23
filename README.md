# Automatización POM Saucedemo con Appium + Pytest
Este repositorio contiene una estructura POM con la cual se automatizaron las pruebas del flujo de login en la aplicación Saucedemo, 
utilizando las siguientes herramientas:
- Pytest
- Allure 
- Flake8 
## Requerimientos previos
Se requiere tener instalado:
- Android Studio 
- IDE: PyCharm
- Appium server
- Appium inspector

## Configuración del proyecto
Desde PyCharm ir a las preferencias del proyecto, ahí elegir como python interpreter una versión de python 3 o superior, adicional instalar las siguientes librerías:
- Test Runner: Pytest
- Appium-Python-Client
- allure-pytest
- allure-python-commons
- flake8

##APK
El apk utilizado para la creación de los casos de prueba se localiza en la carpeta `App`.
##Capabilities 
Para  este proyecto se utilizo un emulador Pixel XL con android 11, en caso de requerir cambiar las capabilities estás se tendrán que editar en el `conftest.py`  del proyecto:
```bash
{
    "platformName": "Android",
    "appium:platformVersion": "11",
    "appium:deviceName": "PixelXL",
    "appium:automationName": "UiAutomator2",
    "appium:app":
        "ruta donde se encuentra el apk"
}
```
## Usuarios de prueba
En el archivo `pytest.ini` se deberán agregar los datos de los usuarios necesarios para las pruebas, completando la siguiente información:
```bash
{
    USERNAMESUCCESS=
    PASSWORDSUCCESS=
    USERNAMENONEXISTENT=
    NODATA=
    USERNAMEWITHEMOJI=
}
```
## Ejecución de tests 
#### Ejecutar todos los tests de inicio de sesión

 pytest 
```
#### Ejecutar pruebas de regresión
```bash
  pytest -m regression
```
#### Ejecutar pruebas de humo
```bash
  pytest -m smoke
```
#### Ejecutar generar reporte con allure
Generación de reportes:
```bash
  py.test --alluredir=reportes ./tests
  
  allure serve reportes
```
###Generación de reportes por mark de la prueba

```bash
 pytest -m smoke  --alluredir=reportes ./tests
 allure serve reportes
```
### Análisis de código estático 

Se utiliza la herramienta flake8 para el análisis de código estático:
```bash
 flake8 ./carpeta_a_analizar
```
En el caso de proyecto se validaron:
```bash
 flake8 ./screens
```
```bash
 flake8 ./tests
```
```bash
 flake8 ./utils
```
