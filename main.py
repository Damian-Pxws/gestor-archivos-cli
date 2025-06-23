# Lógica principal del gestor CLI

# main.py
import os
from utils.file_operations import list_files, copy_file, move_file, delete_file, create_folder

def main():
    while True:
        print("\n=== Gestor de Archivos CLI ===")
        print("1. Listar archivos")
        print("2. Copiar archivo")
        print("3. Mover archivo")
        print("4. Borrar archivo")
        print("5. Crear carpeta")
        print("6. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            ruta = input("Introduce la ruta del directorio: ")
            list_files(ruta)
        elif opcion == '2':
            origen = input("Ruta del archivo a copiar: ")
            destino = input("Ruta de destino: ")
            copy_file(origen, destino)
        elif opcion == '3':
            origen = input("Ruta del archivo a mover: ")
            destino = input("Ruta de destino: ")
            move_file(origen, destino)
        elif opcion == '4':
            ruta = input("Ruta del archivo a borrar: ")
            delete_file(ruta)
        elif opcion == '5':
            ruta = input("Ruta donde crear la carpeta: ")
            create_folder(ruta)
        elif opcion == '6':
            print("Saliendo del Gestor de Archivos CLI...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()