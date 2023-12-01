"""
27/11/2023

Práctica del examen para realizar en casa
-----------------------------------------

* El programa debe estar correctamente documentado.

* Debes intentar ajustarte lo máximo que puedas a lo que se pide en los comentarios TODO.

* Tienes libertad para desarrollar los métodos o funciones que consideres, pero estás obligado a usar como mínimo todos los que se solicitan en los comentarios TODO.

* Además, tu programa deberá pasar correctamente las pruebas unitarias que se adjuntan en el fichero test_agenda.py, por lo que estás obligado a desarrollar los métodos que se importan y prueban en la misma: pedir_email(), validar_email() y validar_telefono()

"""

import os
import pathlib
from os import path

# Constantes globales
RUTA = pathlib.Path(__file__).parent.absolute() 

NOMBRE_FICHERO = 'contactos.csv'

RUTA_FICHERO = path.join(RUTA, NOMBRE_FICHERO)

#TODO: Crear un conjunto con las posibles opciones del menú de la agenda
OPCIONES_MENU = {"1", "2", "3", "4", "5", "6", "7", "8"}
#TODO: Utiliza este conjunto en las funciones agenda() y pedir_opcion()

def mostrar_menu():
    """ Muestra el menú de la agenda
    """
    opciones_menu = [
        "Nuevo contacto",
        "Modificar contacto",
        "Eliminar contacto",
        "Vaciar agenda",
        "Cargar agenda inicial",
        "Mostrar contactos por criterio",
        "Mostrar la agenda completa",
        "Salir"
    ]

    print("\nMENU")
    print("---------------------------")

    for i in range(len(opciones_menu)):
        print(f"{i+1}. {opciones_menu[i]}")

    print("\nSeleccione una opción: ", end="")


def borrar_consola():
    """ Limpia la consola
    """
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")


def cargar_contactos(contactos: list):
    """ Carga los contactos iniciales de la agenda desde un fichero
    ...
    """
    """#TODO: Controlar los posibles problemas derivados del uso de ficheros...

    PARAMETROS
    ----------
    contactos : list
        Lista que se rellenará con la información del archivo"""
    
    try:
        with open(RUTA_FICHERO, 'r') as fichero:
            for linea in fichero:
                partes = linea.strip().split(';')

                contacto = {
                    "nombre": partes[0],
                    "apellido": partes.get(1, ""),
                    "email": partes.get(2, ""),
                    "telefonos": partes[3:] if len(partes) > 3 else []
                }


                contactos.append(contacto)

        print("Contactos cargados exitosamente.")

    except Exception:
        print("No se pudieron cargar los contactos.")

def agregar_contacto(contactos: list):
    """
    Crea un diccionario que representa un contacto

    PARAMETROS
    ----------
    contactos : list
        Lista de contactos donde se va a agregar un registro
    """

    
    nombre = input("Ingrese el nombre: ").strip()
    apellido = input("Ingrese el apellido: ").strip()
    email = input("Ingrese el email: ").strip()

    telefonos = []
    salir = False
    while not salir:
        telefono = input("Ingrese un teléfono (no introducir nada para salir): ")
        if telefono == "":
            salir=True
        telefonos.append(telefono)

    nuevo_contacto = {
        "nombre": nombre,
        "apellido": apellido,
        "email": email,
        "telefonos": telefonos
    }

    contactos.append(nuevo_contacto)



def modificar_contacto(contactos: list):
    """
    Modifica la información de un contacto

    PARAMETROS
    ----------
    contactos : list
        Lista de contactos a modificar
    """
    email_actual = input("Ingrese el email del contacto que desea modificar: ").strip().lower()

    # Buscar la posición del contacto en la lista
    posicion = buscar_contacto(contactos, email_actual)

    if posicion != None:
        contacto = contactos[posicion]

        print("\nInformación actual del contacto:")
        mostrar_contacto(contacto)

        nuevo_nombre = input("Ingrese el nuevo nombre (no introducir nada para no actualizar): ").strip()
        nuevo_apellido = input("Ingrese el nuevo apellido (no introducir nada para no actualizar): ").strip()
        nuevo_email = input("Ingrese el nuevo email (no introducir nada para no actualizar): ").strip()

        if nuevo_nombre:
            contacto["nombre"] = nuevo_nombre.title()
        if nuevo_apellido:
            contacto["apellido"] = nuevo_apellido.title()
        if nuevo_email:
            contacto["email"] = nuevo_email

        print("\nContacto modificado")

        print("\nInformación actualizada del contacto:")
        mostrar_contacto(contacto)
    else:
        print("\nNo se encontró el contacto para modificar.")

    pulse_tecla_para_continuar()
    borrar_consola()


def vaciar_agenda(contactos: list):
    """
    Vacia la agenda, eliminando todos los contactos

    PARAMETROS
    ----------
    contactos : list
        Lista de contactos donde se va a vaciar todo
    """

    confirmar = input("¿Está seguro de que desea vaciar la agenda? (si/no): ").lower()

    salir = False

    while not salir:
        if confirmar == "si":
            contactos.clear()
            print("La agenda se ha vaciado")
            salir = True
        elif confirmar == "no":
            print("No se ha vaciado la agenda")
            salir = True
        else:
            print("Error, introduce una opción correcta")


def mostrar_contactos_por_criterio(contactos : list):
    #Este me falta
    return None
    

def mostrar_contactos(contactos: list):
    """
    Muestra todos los contactos de la agenda 

    PARAMETROS
    ----------
    contactos : list
        Lista de contactos que se van a mostrar
    """
    if not contactos:
        print("La agenda está vacía.")
    else:
        print("\nREGISTROS")
        print("--------------------------")

        def clave(contacto):
            return contacto["nombre"].lower()

        for contacto in sorted(contactos, key=clave):
            mostrar_contacto(contacto)


def mostrar_contacto(contacto):
    """
    Muestra un contacto en un formato específico

    PARAMETROS
    ----------
    contacto : dict
    diccionario donde se van a guardar los datos
        
    """
    print(f"Nombre: {contacto["nombre"]} {contacto["apellido"]}")
    print(f"Email: {contacto["email"]}")
    if contacto["telefonos"]:
        print("Teléfonos:", " - ".join(contacto["telefonos"]))
        print("\n")
    else:
        print("Teléfonos: ninguno")
        print("\n")


def eliminar_contacto(contactos: list):
    """
    Elimina un contacto de la agenda

    PARAMETROS
    ----------
    contactos : list
        Lista de contactos donde se va a eliminar el contacto
    """

    try:
        eliminado = input("Ingrese el email del contacto que desea eliminar: ").strip().lower()

        # TODO: Crear función buscar_contacto para recuperar la posición de un contacto con un email determinado
        pos = buscar_contacto(contactos, eliminado)

        if pos != None:
            del contactos[pos]
            print("Se eliminó 1 contacto")
        else:
            print("No se encontró el contacto para eliminar")
    except Exception as e:
        print(f"**Error** {e}")
        print("No se eliminó ningún contacto")

# Luego puedes llamar a esta función desde tu función principal (main) con:
# eliminar_contacto(contactos)


def pedir_opcion():
    """ Pide al usuario que ingrese una opción del menú y la devuelve
    """
    opcion = input("Seleccione una opción: ")
    return opcion
    
def agenda(contactos: list):
    """
    Ejecuta el menú de la agenda con varias opciones

    PARAMETROS
    ----------
    contactos : list
        Lista de contactos a partir de la cual se van a ejecutar las opciones

    """
    """#TODO: Crear un bucle para mostrar el menú y ejecutar las funciones necesarias según la opción seleccionada...
        #TODO: Se valorará que utilices la diferencia simétrica de conjuntos para comprobar que la opción es un número entero del 1 al 6"""    
    opcion = None

    while opcion != "8":
        mostrar_menu()
        opcion = pedir_opcion()

        opciones_validas = set(OPCIONES_MENU)

        if opcion not in opciones_validas:
            print("Opción no válida. Introduce un número del 1 al 8.")
        else:
            if opcion == "1":
                agregar_contacto(contactos)
            elif opcion == "2":
                modificar_contacto(contactos)
            elif opcion == "3":
                eliminar_contacto(contactos)
            elif opcion == "4":
                vaciar_agenda(contactos)
            elif opcion == "5":
                cargar_contactos(contactos)
            elif opcion == "6":
                mostrar_contactos_por_criterio(contactos)
            elif opcion == "7":
                mostrar_contactos(contactos)
            elif opcion == "8":
                print("\nSaliendo del programa...")
            
        pulse_tecla_para_continuar()
        borrar_consola()


def buscar_contacto(contactos: list, email: str):
    """ Busca un contacto en la lista por su email y devuelve la posición si lo encuentra


    PARAMETROS
    ----------
    contactos : list
        Lista de contactos donde se va a agregar un registro
    email : str
        email a partir del cual se va a buscar al contacto
    """
    
    for posicion in range(len(contactos)):
        if contactos[posicion].get("email") == email:
            return posicion

    return None


def pulse_tecla_para_continuar():
    """ Muestra un mensaje y realiza una pausa hasta que se pulse una tecla
    """
    print("\n")
    os.system("pause")


def main():
    """ Función principal del programa
    """
    borrar_consola()

    #TODO: Asignar una estructura de datos vacía para trabajar con la agenda
    contactos = []

    cargar_contactos(contactos)

    agenda(contactos)


if __name__ == "__main__":
    main()