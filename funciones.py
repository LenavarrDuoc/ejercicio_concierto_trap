import os, time
TUPLA_TIPO_ENTRADA = ("G", "V")
WAIT = 3

compras = []
def wait(wait):
    time.sleep(wait)

def clear():
    """Limpia pantalla en terminales de Sistemas Operativos Windows y de Based-on-Unix."""
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')

def validar_nombre(mensaje:str):
    while True:
        nombre = input(mensaje).strip().title()
        
        search = consultar_compras(nombre)
        if search[0]:
            print("Nombre ya existe. Debe elegir otro nombre.")
        elif not search[0]:
            print(f"Nombre ingresado {nombre}")
            input(("presione cualquier tecla..."))
            break
        input(("presione cualquier tecla..."))


def generar_titulos(title = "", subtitle = ""):
    """Genera títulos dado un título y un subtítulo en los argumentos 'title' y 'subtitle'"""
    print("\t" + title.center((len(title) + 8), "="))
    print(subtitle.center((len(subtitle) + 4), "-"))

def generar_compra(title = "", subtitle = ""):
    """Solicita ingreso de datos de nombre de comprador, tipo de entrada a comprar, y un código de confirmación para realizar la compra del ticket.
    Argumentos: 'title' = se ingresa un título para todo el proceso de compras (vacío por defecto). | subtitle =  se genera un subtítulo para todo el proceso de compras (vacío por defecto)."""
    customer_name = input("Ingrese nombre de comprador: ")

    ticket_type = input("Ingrese el tipo de entrada a comprar ('G' para general. 'V' para VIP): ")

    confirmation_code = input("Ingrese código de confirmación.\n( Mínimos: 6 de largo, 1 letra mayúscula, 1 número, sin espacios en blanco): ")

    compra = {
        'comprador' : customer_name,
        'tipo_de_entrada' : ticket_type,
        'codigo_de_confirmacion' : confirmation_code
    }

    compras.append(compra)
    print(f"Se ha generado la venta exitósamente:\n-Comprador: {customer_name}.\n-Tipo de entrada: {ticket_type}.\n-Código de confirmación: {confirmation_code}.")

def consultar_compras(search_value = "", title= "", subtitle= ""):
    """Busca los elementos de la lista indicada en el argumento e imprime su contenido. De no haber contenido, imprime que la lista está vacía."""
    found = False
    inventario = True
    posicion = 0
    clear()
    if len(compras) == 0:
            generar_titulos(title, subtitle)
            print("La lista está vacía. Aún no hay ingresos.")
    else:
        while inventario:
            clear()
            generar_titulos(title, subtitle)
            search_value = input("Ingrese nombre del comprador a buscar: ")
            for x in (compras):
                if x['comprador'] == search_value:
                    found = True
                    posicion = compras.index(x)
                    contenido_x = str(x).replace("{", "").replace("}", "").replace("'", "").replace("[", "").replace("]", "").replace(",", " |").replace("_", " ").replace('G', "General").replace('V', "VIP")
                    print(f"Venta n°{posicion + 1 } => " + contenido_x.title())
                    inventario = False
                    break
                else:
                    print("El comprador no se encuentra.")
                    input("(presione cualquier tecla para continuar...)")
    return found, posicion, len(compras)

def cancelar_compra(title, subtitle):
    while True:
        clear()
        search = consultar_compras("",title, subtitle)
        if search[2] == 0:
            break
        elif not search[0]:
            input("(presione cualquier tecla para continuar...)")
        elif search[0]:
            opt = input("¿Desea remover esta compra?\n1. Sí.\n2. No.\n:")
            if opt == "1":
                posicion = search[1]
                compras.pop(posicion)
                print("Se ha borrado la compra.")
                break
            elif opt == "2":
                print("No se generaron cambios.")
                break
            else:
                print("ERROR: Debe ingresar una opción numérica disponible en el menú.")
                input("(presione cualquier tecla para continuar...)")
        