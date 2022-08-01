from pathlib import Path

# encontrar todos los archivos csv que contienen el texto "buscar_texto" en su nombre de archivo
carpeta = Path('2022-csv-renombrado')
buscar_texto = '202201'

for path in carpeta.glob('**/*.csv'):
    # print(path)
    if buscar_texto in path.name:
        print(path)  # ruta relativa
        print(path.absolute())  # ruta absoluta

