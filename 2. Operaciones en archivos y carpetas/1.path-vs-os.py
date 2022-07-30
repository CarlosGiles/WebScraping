# Importamos el módulo Path desde la librería pathlib
from pathlib import Path
# Importamos el módulo os
import os

"""
Obtener directorio donde nos encontramos usando el modulo OS y Path:
con la función getcwd() para os y la función cwd() para Path obtenesmo la dirección en que se está
trabajando
"""
# Guardamos nuestra ubicación en la variable path_os y path_Path
path_os = os.getcwd()
path_Path = Path.cwd()

# Imprimir el tipo de cada objeto para verificar
print(type(path_os))
print(type(path_Path))

"""
Partes de un path:
Una ruta o path es en sí la ubicación de un archivo o carpeta, el último elemento o eslabon es entonces 
el archivo que nos interesa. Para obtener cada parte de un path, crearemos uno y veremos cómo
manipularlo.

Cabe aclarar que al crear un objeto y ruta con el módulo Path, solo se crea a nivel de código, no se
crea el archivo en el directorio
"""
# Creamos una variable u objeto del tipo Path llamado "path" y definimos su ruta
path = Path('test/expenses.txt')
# Mostramos en pantalla el obj
print("Este es el path creado: ",path)
# Con el argumento "parts" se muestran las partes de la ruta, el contenido entre cada "/"
print("Las partes del path son: ",path.parts)
# Con "name" se muestra el elemento final del path, el archivo
print("El archivo es: ",path.name)
# "stem" es el nombre del archivo sin la extensión detipo
print("El nombre es: ",path.stem)
# "suffix" devuelve la extensión del tipo de archivo
print("Tipo de archivo: ",path.suffix)