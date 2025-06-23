# Funciones para operaciones de archivos
# utils/file_operations.py
import os
import shutil

def list_files(directory):
    try:
        files = os.listdir(directory)
        print("\nArchivos y carpetas en", directory)
        for file in files:
            print(file)
    except FileNotFoundError:
        print("El directorio no existe.")

def copy_file(source, destination):
    try:
        shutil.copy(source, destination)
        print("Archivo copiado exitosamente.")
    except FileNotFoundError:
        print("El archivo de origen no existe.")
    except Exception as e:
        print(f"Error al copiar el archivo: {e}")

def move_file(source, destination):
    try:
        shutil.move(source, destination)
        print("Archivo movido exitosamente.")
    except FileNotFoundError:
        print("El archivo de origen no existe.")
    except Exception as e:
        print(f"Error al mover el archivo: {e}")

def delete_file(path):
    try:
        os.remove(path)
        print("Archivo borrado exitosamente.")
    except FileNotFoundError:
        print("El archivo no existe.")
    except Exception as e:
        print(f"Error al borrar el archivo: {e}")

def create_folder(path):
    try:
        os.makedirs(path, exist_ok=True)
        print("Carpeta creada exitosamente.")
    except Exception as e:
        print(f"Error al crear la carpeta: {e}")