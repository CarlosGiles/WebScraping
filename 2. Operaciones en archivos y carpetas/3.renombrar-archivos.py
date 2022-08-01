from pathlib import Path

"""
Se creará el objeto tipo Path llamado path que define una carpeta test. Las carpeta "test" ya fue creada en el
directorio manualmente, el código siguiente solo le cambiará el nombre por "nuevo_test"
"""
# 1. Renombrar nombre carpeta
path = Path('test')
path.rename('nuevo_test')

"""
Tenemos un archivo de texto lamado gastos.txt y cambiaremos el nombre a gastos-enero.txt. Para ello creamos el objeto path
con la ruta del archivo y en un nuevo objeto llamado nuevo_nombre_path, que utiliza el método .with_name(), indicamos 
el nuevo nombre.
"""
# 2. Renombrar archivo dentro de una carpeta
path = Path('nuevo_test/gastos.txt')
nuevo_nombre_path = path.with_name('gastos-enero.txt')
# hasta ahora solo indicamos el cambio del nombre en la ruta, verificamos con este print
print(nuevo_nombre_path)
# para efectuar el cambio en el archivo usamos el método tename()
path.rename(nuevo_nombre_path)

"""
Anteriormente se crearon automáticamente una carpeta 2022 y subcarpetas con meses y días. Los subdirectorios 
inmediatos de una carpeta son los archivos y carpetas dentro de esa carpeta.
"""
# 3. Obtener path de los subdirectorios immediatos
# para las RUTAS DE LAS SUBCARPETAS INMEDIATAS creamos el objeto carpeta de tipo Path que se llamará 2022
carpeta = Path('2022')
# el método iterdir() va iterando dentro de la carpeta indicada, convertimos "carpeta" en una lista para iterar con for
for path in list(carpeta.iterdir()):
    print(path)
"""
Enseguida obtendremos la ruta de los subdirectorios inmediatos pero también los subdirectorios de estos. Usaremos los
caracteres especiales **/* donde:

** --> represente este directorio y sus subdirectorios
/* --> representa a las cadenas de texto de los nombres de los directorios
**/* --> indica que queremos obtener todos los dirctorios y subdirectorios sin importar el nombre y extensión
"""
# 4. Obtener path de todos subdirectorios
# utilizamos el método glob() con argumento "**/*"
paths = carpeta.glob('**/*')
for path in paths:
    print(path)

"""
También podemos obtener la ruta de las carpetas que contengan un archivo (que no estén vacías) con el método .is_file()
"""
# 5. Obtener path de todos los subdirectorios con un archivo
carpeta_archivos = Path('2022archivos')
paths_archivos = carpeta_archivos.glob('**/*')
for path in paths_archivos:
    if path.is_file():
        print(path)
"""
Podemos obtener el path de los directorios que contengan un tip de archivo en específico por su extensión. Este script
de python se encuentra en una carpeta donde todos los archivos del mismo tipo, están en este misma carpeta. Las demás 
carpetas contienen archivos de texto y csv. 

Para trabjar con la ruta en la que se encuentra este mismo script, usamos Path('.')
**/*.py --> obtene todos los directorios de este directorio con cadena de texto .py
"""
# 6. Obtener path de todos los subdirectorios que tienen archivos .py
carpeta_archivos_py = Path('.')
for path in carpeta_archivos_py.glob('**/*.py'):
    print(path)

# ATENCIÓN
"""
Este escript da error si no se comentan los ragmentos de código que se van ejecutando
"""
# ATENCIÓN














