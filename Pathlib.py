from pathlib import Path, PureWindowsPath

carpeta = Path('C:/Users/Asus/Desktop/Pyhton/DIA 6/prueba.txt')

ruta_windows = PureWindowsPath(carpeta)
print(ruta_windows)

print(carpeta.read_text())
print(carpeta.name)
print(carpeta.suffix)
print(carpeta.stem)

if not carpeta.exists():
    print("Vales monda, no existe")
else:
    print("Genial care verga si existe")
