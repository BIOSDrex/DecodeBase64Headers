import base64
import re

rutaLog = r'C:\Ejercicio_JCA\PythonDesencrypted\access.log'

#Expresion regular para la busqueda del patron base64
patron = r'"Basic ([A-Za-z0-9+/=]+)"'

#Almacen de resultados
lista_guardar = []

with open(rutaLog,'r', encoding='utf-8') as archivo:
    for linea in archivo:
        # Desencriptar base64 encontrado
        match = re.search(patron, linea)
        # Condicion para encontrar la coincidencia y capturarla
        if match:
            b64_capture = match.group(1)
            try:
                # Imprimimos la decodificación
                decode = base64.b64decode(b64_capture).decode('utf-8')
                lista_guardar.append((b64_capture, decode))
            except Exception as e:
                print(f'Error al decodificar')
#Mostramos resultados
for org, decode in lista_guardar:
    print(f'Base64: "{org}" --> Decodificado: {decode}')

#Guardamos en un archivo
with open('Decode.txt', 'w', encoding='utf-8') as salida:
    for org, decode in lista_guardar:
        salida.write(f'{org},{decode}\n')

__author__ = "Andres Felipe Merlano Pineda"
__date__ = "07/05/2025"
__version__ = "1.0.0"








