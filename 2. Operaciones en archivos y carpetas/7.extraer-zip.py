from pathlib import Path
import zipfile

# extraer zip en carpeta "temp"
directorio_actual = Path('.')
directorio_objetivo = Path('temp')

for path in directorio_actual.glob('*.zip'):
    print(path)
    with zipfile.ZipFile(path, 'r') as zip_obj:
        zip_obj.extractall(path=directorio_objetivo)
