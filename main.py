from funciones import *
MAIN_TITLE = "SISTEMA DE VENTA DE ENTRADAS"
OPT1_TITLE = "Compra de entrada"
SUBTITLE = "Concierto de Trap con el 'Conejo Simpático'"

MAIN_MENU = f"""
Opciones:
1. Comprar entrada.
2. COnsultar comprador.
3. Cancelar compra.
4. Salir."""

while True:
    clear()
    generar_titulos(MAIN_TITLE,SUBTITLE)
    print(MAIN_MENU)
    opt = input("Ingrese una opción disponible del menú: ")
    clear()
    if opt == "1":
        generar_compra(OPT1_TITLE, SUBTITLE)
    elif opt == "2":
        pass
    elif opt == "3":
        pass
    elif opt == "4":
        print("Gracias por su preferencia. Adiós!")
        break
    else:
        print("ERROR: Debe ingresar una opción numérica disponible en el menú.")
    input("(presione cualquier tecla para continuar...)")