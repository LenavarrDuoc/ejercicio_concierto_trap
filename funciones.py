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

def validar_nombre(mensaje:str, title="", subtitle=""):
    nombre = ""
    while True:
        clear()
        generar_titulos(title, subtitle)
        nombre = input(mensaje).strip().title()
        nombre_split = nombre.split()
        if nombre.find("  ") != -1:
            print("ERROR: Debe haber solo un espacio entre nombres.")
        elif not nombre.replace(" ","").isalpha():
            print("ERROR: Debe ingresar un valor alfabético.")
        elif len(nombre) == len(nombre.replace(" ", "")):
            print("ERROR: Debe ingresar tanto Nombre como Apellido datos")
        elif len(nombre_split[0]) < 2 or len(nombre_split[1]) < 2:
            print("ERROR: Nombre y Apellido deben ser de mínimo 2 caracteres de largo cada uno.")
        else:
            return nombre
        input("(presione cualquier tecla para continuar...)")
    
def validar_tipo_entrada(mensaje:str, title = "", subtitle = ""):
    while True:
        clear()
        generar_titulos(title, subtitle)
        print(f"Tipos de entradas disponibles: {TUPLA_TIPO_ENTRADA}")
        tipo = input(mensaje).strip().upper()
        if not tipo in (TUPLA_TIPO_ENTRADA):
            print("ERROR: Debe ingresar una de las opciones disponibles")
        else:
            print(f"Tipo de entrada ingresada: {tipo}.")
            return tipo
        input("(presione cualquier tecla para continuar...)")

def validar_codigo(mensaje:str, title = "", subtitle = ""):
    while True:
        clear()
        generar_titulos(title, subtitle)
        code = input(mensaje).strip().replace(" ","").lower().title()
        if not code.isalnum():
            print("ERROR: Debe ingresar un código alfanumérico (números y letras) sin caracteres especiales.")
        elif len(code) < 6:
            print("ERROR: El código debe ser de un largo mínimo de 6 caracteres.")
        else:
            return code
        input("(presione cualquier tecla para continuar...)")

def generar_titulos(title = "", subtitle = ""):
    """Genera títulos dado un título y un subtítulo en los argumentos 'title' y 'subtitle'"""
    print("\t" + title.center((len(title) + 8), "="))
    print(subtitle.center((len(subtitle) + 4), "-"))

def generar_compra(title = "", subtitle = ""):
    """Solicita ingreso de datos de nombre de comprador, tipo de entrada a comprar, y un código de confirmación para realizar la compra del ticket.
    Argumentos: 'title' = se ingresa un título para todo el proceso de compras (vacío por defecto). | subtitle =  se genera un subtítulo para todo el proceso de compras (vacío por defecto)."""
    while True:
        search_name = consultar_compras("", title, subtitle, 1)
        if search_name[0]:
            print("Nombre ya existe. Debe ingresar un nombre distinto.")
            input("(presione cualquier tecla para continuar...)")  
        else:
            customer_name = search_name[2]
            print(f"Nombre ingresado {customer_name}")
            input("(presione cualquier tecla para continuar...)")
            break

    ticket_type = validar_tipo_entrada("Ingrese el tipo de entrada a comprar ('G' para general. 'V' para VIP): ", title, subtitle)

    confirmation_code = validar_codigo("Ingrese código de confirmación.\n( Mínimos: 6 de largo, 1 letra mayúscula, 1 número, sin espacios en blanco): ", title, subtitle)

    compra = {
        'comprador' : customer_name,
        'tipo_de_entrada' : ticket_type,
        'codigo_de_confirmacion' : confirmation_code
    }

    compras.append(compra)
    print(f"Se ha generado la venta exitósamente:\n-Comprador: {customer_name}.\n-Tipo de entrada: {ticket_type}.\n-Código de confirmación: {confirmation_code}.")

def consultar_compras(search_value = "",title = "", subtitle = "", imprimir = 0):
    """Busca los elementos de la lista indicada en el argumento e imprime su contenido. De no haber contenido, imprime que la lista está vacía."""
    found = False
    posicion = 0
    found_information_str = ""
    if len(compras) == 0:
        if imprimir == 0:
            clear()
            generar_titulos(title, subtitle)
            print("La lista está vacía. Aún no hay ingresos.")
        else:
            search_value = validar_nombre("Ingrese nombre y apellido de comprador: ", title, subtitle)
    else:
        if search_value == "":
            search_value = validar_nombre("Ingrese nombre y apellido de comprador: ", title, subtitle)
        if imprimir == 0:
            clear()
            generar_titulos(title, subtitle)
        for x in (compras):
            if x['comprador'] == search_value:
                found = True
                posicion = compras.index(x)
                if imprimir == 0:
                    contenido_x = str(x).replace("{", "").replace("}", "").replace("'", "").replace("[", "").replace("]", "").replace(",", " |").replace("_", " ").replace('G', "General").replace('V', "VIP")
                    found_information_str = f"Venta n°{posicion + 1 } => " + contenido_x.title()
                    print(found_information_str)
        if found == False and imprimir == 0:
            print("No se ha encontrado a cliente indicado.")
    return found, posicion, search_value, found_information_str

def cancelar_compra(title, subtitle, imprimir=0):
    clear()
    search = consultar_compras("", title, subtitle,imprimir)
    if search[0]:
        while True:
            clear()
            generar_titulos(title, subtitle)
            print(search[3])
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
        