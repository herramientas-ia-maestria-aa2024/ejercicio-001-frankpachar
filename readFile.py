# developer: Franklin Pachar
def readFile(fileName):
    try:
        # Abre el archivo en modo lectura
        with (open(fileName, 'r') as archivo):
            # Lee todas las líneas del archivo
            lines = archivo.readlines()
            # Imprime cada línea del archivo
            for line in lines:
                print(line.strip())  # strip() elimina los espacios en blanco al inicio y al final de la línea
    except FileNotFoundError:
        print(f"El archivo '{fileName}' no existe.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Nombre del archivo que quieres leer
fileName = 'datafile.txt'

# Llama a la función para leer el archivo
readFile(fileName)