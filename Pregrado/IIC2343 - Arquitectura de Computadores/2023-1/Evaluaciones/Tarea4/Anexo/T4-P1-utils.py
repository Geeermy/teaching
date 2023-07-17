import argparse
import math

# Función para transformar un número entero "number" a binario con una cantidad
# de "bits_n" bits.
def int_to_binary(number, bits_n):
    return format(number, 'b').zfill(bits_n)
 
# Función para obtener el logaritmo en base 2 de un número.
def log_2(number):
    return int(math.log2(number))

# Obtención de la ruta de archivo como argumento de consola.
# Ejemplo: > python3 T4-P1-utils.py input.txt
# Si el archivo no existe, arrojará un error. Puede asumir que solo se probarán
# rutas de archivo válidas.
parser = argparse.ArgumentParser()
parser.add_argument('filename', type=argparse.FileType('r'))
args = parser.parse_args()
filename = args.filename

with filename as f:
    line = f.readline()
    while line:
        print(line.strip())
        line = f.readline()
