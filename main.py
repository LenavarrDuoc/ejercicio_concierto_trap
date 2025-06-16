from funciones import *
MAIN_TITLE = "SISTEMA DE VENTA DE ENTRADAS"
OPT1_TITLE = "Compra de entrada"
OPT2_TITLE = "Consultar comprador"
OPT3_TITLE = "Cancelar compra"
SUBTITLE = "Concierto de Trap con el 'Conejo Simpático'"

MAIN_MENU = f"""
Opciones:
1. Comprar entrada.
2. Consultar comprador.
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
        consultar_compras("",OPT2_TITLE, SUBTITLE, 0)
    elif opt == "3":
        cancelar_compra(OPT3_TITLE, SUBTITLE, 0)
    elif opt == "4":
        print("Gracias por su preferencia. Adiós!")
        break
    else:
        print("ERROR: Debe ingresar una opción numérica disponible en el menú.")
    input("(presione cualquier tecla para continuar...)")