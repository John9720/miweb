Se debe crear una DB (recomendado MySQL) dado que se maneja una conexión de esta naturaleza

'''sql

CREATE DATABASE nombre_base_datos;

Configuración de la DB.

DB_HOST = 'localhost' # o la IP/URL de tu servidor 
MySQL DB_USER = 'root' # Usuario de MySQL 
DB_PASS = 'tu_contraseña' # Contraseña del usuario 
DB_NAME = 'nombre_base_datos' # Nombre de la base de datos que creaste

En el proyecto ya están preconfiguradas las conexiones, solo se debe crear una DB propia y cambiar los datos
