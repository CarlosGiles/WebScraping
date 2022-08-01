"""
En la carpeta "2022archivos" tenemos el archivo "gastos.csv" en varias carpetas. Podemos renombrarlo basándonos en 
los nombres de las carpetas padre (2022, meses, dias). El formato final seria "gastosYYYYMMDD.csv"
"""
from pathlib import Path
import re #Módulo para expresiones regulares
# Este script devuelve por partes las rutas en las que existe dicho archivo 
# Renombrar "gastos.csv" basado en los nombres de carpetas padre
carpeta = Path('2022archivos')
paths = carpeta.glob('**/*.csv')
for path in paths:
    print(path.parts)