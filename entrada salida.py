mi_archivo = open('prueba.txt')

print(mi_archivo.read())

mi_archivo.close()

mi_archivo = open('prueba.txt')

print(mi_archivo.readline())


una_linea = mi_archivo.readline()
print(una_linea.upper())

una_linea = mi_archivo.readline()
print(una_linea.rstrip())




for l in mi_archivo:
    print("aca dice: " + l)
