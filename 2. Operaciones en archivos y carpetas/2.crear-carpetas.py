"""
En este script se automatiza la creación de carpetas nombradas con días y meses. Para ello se utiliza una 
librería de Python llamada calendar 
"""
# Para crear carpetas importamos módulo Path
from pathlib import Path
# Importamos la librería que nos permite trabajar con el calendario
import calendar

# 1.Crear una sola carpeta con el método mkdir(), en la ruta que se está trabajando el script
Path('nueva_carpeta(1)').mkdir()
# Podemos pasar argumentos al método para evitar un error si se intenta crear una carpeta que ya existe
Path('nueva_carpeta(1)').mkdir(exist_ok=True)

"""
Anteriormente ya fue creada la carpeta "nueva_carpeta(1)", con el parámetro "parents=True" se crearán las
carpetas necesarias (faltantes) de una ruta indicada
"""
# 2.Crear multiples subcarpetas (parents=True: cualquier carpeta faltante en la ruta se creara de ser necesario)
# Dentro de Path() creamos la ruta deseada
Path('nueva_carpeta(1)/nueva_subcarpeta(2)/nueva_subsubcarpeta(3)').mkdir(parents=True, exist_ok=True)

"""
Creación de multiples carpetas en orden de los meses del año y que incluyan los días como subcarpetas.

La librería calendar tiene un método llamado month_name[:] el cual puede ser convertido en lista con función list
que guardamos en "meses_ano"
"""
# 3.Crear carpeta "2022", subcarpetas desde Enero hasta Diciembre y subsubcarpetas para 5 dias aleatorios (Dia 1, Dia 5, ...)
meses_ano = list(calendar.month_name[1:])
# Lista con 4 elementos nombrados como un número de día del mes
dia_semana = ['Dia 1', 'Dia 8', 'Dia 15', 'Dia 22']

"""
Podemos crear una sentencia simple para dar formato a las carpetas: "2022/Diciembre". Esto indica que la primera
carpeta, carpeta padre, será llamada 2022 y la siguiente carpeta dntro de ella será llamada Diciembre.

Ej: Path("2022/Diciembre").mkdir(parents=True, exist_ok=True)
"""
# Hacemos iteracones para crear las carpetas de los meses dentro de la carpeta 2022 y para los días dentro de los meses
for i, mes in enumerate(meses_ano):
    # Bucle para las carpetas por día
    for dia in dia_semana:
        # La carpeta del mes se ordena con i+1 para que quede dentro de la arpeta 2022 las carpetas "1.Enero/Día 1..."
        Path(f'2022/{i+1}.{mes}/{dia}').mkdir(parents=True, exist_ok=True)#mes y dia cambian con las listas de arriba
