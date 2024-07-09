import pickle

def leer_archivo_pkl(nombre_archivo):
    try:
        with open(nombre_archivo, 'rb') as archivo:
            contenido = pickle.load(archivo)
            return contenido
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no se encontró.")
    except Exception as e:
        print(f"Error al leer el archivo {nombre_archivo}: {e}")

# Reemplaza 'nombre_del_archivo.pkl' con el nombre de tu archivo pkl
nombre_archivo_pkl = './Pruebas 1/walk_002_stageii_pkl_version_synthetic_omegas_quaternions.pkl'

# Llama a la función para leer el archivo pkl
contenido_del_archivo = leer_archivo_pkl(nombre_archivo_pkl)

# Imprime el contenido del archivo
if contenido_del_archivo:
    print("Contenido del archivo pkl:")
    print(contenido_del_archivo)
