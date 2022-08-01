from pathlib import Path
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# crear archivo1, ..., archivo9 (.txt)
for i in numeros:
    with open(f'test{i}.txt', 'w') as file:
        file.write('Hola Mundo!')

# eliminar todos archivos .txt
for path in Path('.').glob('*.txt'):
    print(path)
    path.unlink()

# eliminar todos archivos excepto test9.txt
for path in Path('.').glob('test[1-8].txt'):
    print(path)
    path.unlink()
