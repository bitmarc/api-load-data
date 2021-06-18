# API_LOAD_DATA

###### *última actualización: 18-06-2021* 
___
## Cóntenido:
- [ Inicio](#api-load-data)
- [1. Requisitos](#1-requisitos)
- [2. Clonar repositorio](#2-clonar-repositorio)
- [3. Creacion del entorno virtual](#3-creacion-del-entorno-virtual)
- [4. Instalacion de dependencias](#4-instalacion-de-dependencias)
- [5. Creacion de base de datos](#5-creacion-de-base-de-datos)
- [6. Configurar llaves de acceso](#6-configurar-llaves-de-acceso)
- [7. Ejecutar el servidor](#7-ejecutar-el-servidor)
- [8. Probar el funcionamiento](#8-probar-el-funcionamiento)
- [Contacto](#contacto-del-programador)
___
&nbsp;

>Nota: Se considera el uso del S.O. linux (ubuntu 21.04) con Python 3.8

## 1. Requisitos
Para la instalcion y configuracion del servidor, se requiere el siguiente software: 

- Python 3.8+ (obligatorio)
- Mysql server (obligatorio)
- git
- virtualenv

## 2. Clonar repositorio
Dentro del directorio deceado ejecutar:
```bash
git clone https://github.com/bitmarc/api-load-data.git
```

## 3. Creacion del entorno virtual
Se recomienda el uso de un entorno virtual
2.1. Crear un nuevo entorno con **virtualenv**
```bash
virtualenv -p python3 nombre_entorno 
```
2.2. **Activar el entorno**
```bash
source nombre_entorno/bin/activate
```

## 4. Instalacion de dependencias
Una vez clonado el repositorio y con el entorno activo, ubicarse en la carpeta raíz del proyecto (a la altura del **manage.py**) y ejecutar:
```bash
pip install -r requirements.txt
```

## 5. Creacion de base de datos
Para poder ejecutar el proyecto es necesario crear una base ded atos en MYSQL server, para ello dentro de una terminal ejecutar los siguientes comandos:

5.1. acceder con root a la shell de sql
```bash
sudo mysql -u root -p
```

5.3. Crear una neva base de datos:
```bash
CREATE DATABASE db_name;
```

5.3. Crear un nuevo usaurio:
```bash
CREATE USER 'user_name'@'localhost' IDENTIFIED BY 'password_user';
```

5.4. dar permisos para acceder a la base de datos:
```bash
GRANT ALL PRIVILEGES ON db_name.* TO 'user_name'@'localhost';
FLUSH PRIVILEGES;
```
depués salir de sql shell

## 6. Configurar llaves de acceso
Para configurar el acceso a la base de datos, se debe crear un archivo json llamado secret, esto en la raíz del proyecto a la altura del archivo manage.py.

Desde la terminal:
```bash
touch secret.json
```
Dentro del archivo, configurar los parámetros de:
* nombre de base de datos
* usuario de la base de datos
* password

mendiante la siguiente estructura:

```json
{
    "FILENAME": "secret.json",
    "DB_NAME": "db_name",
    "USER": "user_db",
    "PASSWORD": "password"
}
```
## 7. Ejecutar el servidor
Para ejecutar el servidor, basta con ejecutar el archivo manage.py desde la terminal:

```bash
python manage.py
```
Si la configuración ha sido correcta,  el servidor estará reciviendo peticiones desde: http://127.0.0.1:5000/

## 8. Probar el funcionamiento
Para probar el funcionamiento, puede usar Postman o Insomnia para realizar las peticiones.

A continuación se muestra un resumen de los endpoints disponibles:

| nombre | endpoint | method |
| ------------- | ------------- | ------------- |
| Guardar un nuevo empleado  | api/employee/  | POST |
| Obtener todos los empleados | api/employee/all/<int:page_num>/  | GET |
| detalle de empleado | api/employee/<string:id_user>/  | GET |
| detalle de contrato de empleado | api/contract/<string:id_user>/  | GET |
| cargar archivo de registros | api/employee/load-file/  | POST |


Resultados tras la prueba del endpoint de carga de archivo :
[![captura del resultado tras ejecutar el endpoint para cargar archivo de datos datos](http://drive.google.com/uc?export=view&id=12Lku1nnclKHesxh2xM7Ex7NnPvMVpHZW)](http://drive.google.com/uc?export=view&id=12Lku1nnclKHesxh2xM7Ex7NnPvMVpHZW)


Resultados de visualizaión de los datos:
[![captura de la consola tras cargar datos](http://drive.google.com/uc?export=view&id=1hO95-HNaarhAVcP--1P8yVwvhqUKg9J-)](http://drive.google.com/uc?export=view&id=1hO95-HNaarhAVcP--1P8yVwvhqUKg9J-)

Resultados tras la ejecucion del endpoint de visualización de datos (paginado)
[![captura del resultado tras ejecutar el endpoint de otencion de todos los empleados](http://drive.google.com/uc?export=view&id=1eQkKzLQKUb9seqfwf5rNHLe7XJysRkJL)](http://drive.google.com/uc?export=view&id=1eQkKzLQKUb9seqfwf5rNHLe7XJysRkJL)

Resultados tras la ejecucion del endpoint para ver detalle de empleado y detalle de contrato
[![captura del resultado tras ejecutar el endpoint de detalle de empleado](http://drive.google.com/uc?export=view&id=1kbdF6KzgKt9MRqY8IIRybUezcAh6CQjy)](http://drive.google.com/uc?export=view&id=1kbdF6KzgKt9MRqY8IIRybUezcAh6CQjy)

[![captura del resultado tras ejecutar el endpoint de detalle de empleado](http://drive.google.com/uc?export=view&id=1g_RWOIE_kP8L_PEnvsBka46Dsx3N7OHm)](http://drive.google.com/uc?export=view&id=1g_RWOIE_kP8L_PEnvsBka46Dsx3N7OHm)

Resultados tras la ejecucion del endpoint para guardar un nuevo empleado
[![captura del resultado tras ejecutar el endpoint de detalle de empleado](http://drive.google.com/uc?export=view&id=1-55kQHPcn3wm6zbhzZsIQ003zzlo4wbD)](http://drive.google.com/uc?export=view&id=1-55kQHPcn3wm6zbhzZsIQ003zzlo4wbD)

&nbsp;
&nbsp;
___
### Contacto del programador:
[@hermuslife](https://twitter.com/hermuslife)
marcoarojas.95@gmail.com
&nbsp;
___