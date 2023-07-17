# -*- coding: utf-8 -*-
"""Taller Nº 2 - Tester

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yTVbP0cPoDZJKhzh9AHT3uPhCNNli37X

# INF3591 - Cloud Computing :: Taller Nº 2 - _Tester_
### Profesores: Cristian Ruz, Germán Contreras Sagredo
### Ayudante: Juan Pablo Gastovic

El siguiente Google Colab tiene por objetivo corroborar que su instancia de Amazon RDS no es públicamente accesible y, por otra parte, que su instancia de Amazon EC2 puede acceder a esta.

## _Testing_ - Instancia Amazon RDS

En primer lugar, ejecute la celda a continuación para poder instalar las librerías necesarias para realizar el _testing_.
"""

!pip install PyMySQL

"""Luego, en esta celda complete las variables vacías (dentro de las comillas, sin comillas para el puerto) con los atributos de conectividad de su instancia en RDS."""

# Punto de enlace de la instancia de base de datos.
DATABASE_HOST = ''
# Nombre de la base de datos (NO CONFUNDIR CON EL ID DE LA INSTANCIA).
DATABASE_NAME = ''
# Puerto de la base de datos (por defecto 3306 para motor MySQL).
DATABASE_PORT = 3306
# Nombre de usuario maestro (por defecto "admin" para motor MySQL).
DATABASE_USERNAME = 'admin'
# Contraseña de usuario maestro.
DATABASE_PASSWORD = ''

"""Luego, ejecutaremos la conexión a la base de datos."""

import pymysql
pymysql.connect(
    host=DATABASE_HOST,
    database=DATABASE_NAME,
    port=DATABASE_PORT,
    user=DATABASE_USERNAME,
    password=DATABASE_PASSWORD
)

"""Si la celda anterior se ejecuta y genera error por `Timeout`, entonces configuró su instancia correctamente.

## _Testing_ - Instancia Amazon EC2

Para verificar que su instancia EC2 puede acceder a la base de datos creada en RDS, siga los siguientes pasos.

1. Conéctese a su instancia en EC2 y, en la consola, instale para Python 3 la librería PyMySQL con el siguiente comando: `python3 -m pip install PyMySQL`

2. Cree un archivo Python ejecutando el siguiente comando: `touch test.py`

2. Complete con las credenciales de su instancia RDS la siguiente celda de código. **No es necesario que la ejecute.**
"""

import pymysql
########################### COMPLETAR ESTA SECCIÓN ###########################
# Punto de enlace de la instancia de base de datos.
DATABASE_HOST = ''
# Nombre de la base de datos (NO CONFUNDIR CON EL ID DE LA INSTANCIA).
DATABASE_NAME = ''
# Puerto de la base de datos (por defecto 3306 para motor MySQL).
DATABASE_PORT = 3306
# Nombre de usuario maestro (por defecto "admin" para motor MySQL).
DATABASE_USERNAME = 'admin'
# Contraseña de usuario maestro.
DATABASE_PASSWORD = ''
########################### COMPLETAR ESTA SECCIÓN ###########################

### CONEXIÓN A LA BASE DE DATOS.
db = pymysql.connect(
    host=DATABASE_HOST,
    database=DATABASE_NAME,
    port=DATABASE_PORT,
    user=DATABASE_USERNAME,
    password=DATABASE_PASSWORD
)
cursor = db.cursor()

### CREAR TABLA CON DATOS
create_user_sql = '''
  CREATE TABLE user (
    id SERIAL PRIMARY KEY,
    username VARCHAR(256),
    role VARCHAR(32)
  );
'''
insert_users_sql = '''
  INSERT INTO user (username, role) VALUES
    ('cruz', 'Docente'),
    ('glcontreras', 'Docente'),
    ('jpgastovic', 'Ayudante');
'''
cursor.execute(create_user_sql)
cursor.execute(insert_users_sql)
cursor.connection.commit()

### CONSULTAR TABLA
fetch_users_sql = 'SELECT id, username, role FROM user;'
cursor.execute(fetch_users_sql)
users = cursor.fetchall()
for user in users:
  print(f'ID: {user[0]}\nNombre de usuario: {user[1]}\nRol: {user[2]}')
  print('-'*20)

### ELIMINAR TABLA
drop_user_table_sql = 'DROP TABLE user;'
cursor.execute(drop_user_table_sql)
cursor.connection.commit()

"""4. Completadas las credenciales, copie este código y péguelo en el archivo `test.py` creado. Para poder editar el archivo desde consola, ejecute el siguiente comando: `nano test.py`

5. Terminado el pegado, con la siguiente secuencia guarda los cambios: `Ctrl+X` (salir del archivo) - `Y` (confirmar cambios) - `Enter` (mantener el nombre del archivo).

6. Finalmente, si todo está en orden, al ejecutar el archivo se imprimirán en consola los usuarios creados en el _tester_ del taller 1: `python3 test.py`
"""