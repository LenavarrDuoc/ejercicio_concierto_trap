
MAIN_MENU = """=== SISTEMA DE VENTA DE ENTRADAS ===
Opciones:
1. Comprar entrada.
2. COnsultar comprador.
3. Cancelar compra.
4. Salir."""

while True:
    print(MAIN_MENU)
    opt = input("Ingrese una opción disponible del menú: ")

    if opt == "1":
        pass
    elif opt == "2":
        pass
    elif opt == "3":
        pass
    elif opt == "4":
        print("Gracias por su preferencia. Adiós!")
        break
    else:
        print("ERROR: Debe ingresar una opción numérica disponible en el menú.")