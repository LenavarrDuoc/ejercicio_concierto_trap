import os, time
TUPLA_TIPO_ENTRADA = ("G", "V")

compras = []

def clear():
    """Limpia pantalla en terminales de Sistemas Operativos Windows y de Based-on-Unix."""
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')
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

def consultar_compras(title, subtitle):
    """Busca los elementos de la lista indicada en el argumento e imprime su contenido. De no haber contenido, imprime que la lista está vacía."""
    found = False
    posicion = 0
    clear()
    if len(compras) == 0:
            generar_titulos(title, subtitle)
            print("La lista está vacía. Aún no hay ingresos.")
    else:
        generar_titulos(title, subtitle)
        search_value = input("Ingrese nombre del comprador a buscar: ")
        for x in (compras):
            if x['comprador'] == search_value:
                found = True
                posicion = compras.index(x)
                contenido_x = str(x).replace("{", "").replace("}", "").replace("'", "").replace("[", "").replace("]", "").replace(",", " |")
                print(f"Venta n°{compras.index(x)} => " + contenido_x)
            else:
                print("El comprador no se encuentra.")
    return found, posicion, len(compras)

def cancelar_compra(title, subtitle, print=0):
    while True:
        search = consultar_compras(title, subtitle, imprimir=0)
        if search[0]:
            break
        opt = input("¿Desea remover esta compra?\.1 Sí.\n2. No.\n:")
        if opt == "1":
            posicion = search[1]
            compras.pop(posicion)
            print("Se ha borrado la compra.")
        elif opt == "2":
            print("No se generaron cambios.")