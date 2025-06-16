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
