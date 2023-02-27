"""Se quiere conservar el historial de los movimientos mensuales en una cuenta corriente.
1. Modificar el tipo CUENTA definido en el capítulo «Estructuras elementales» para conservar el rastro
de los movimientos en una cuenta durante un mes.
2. Establecer el saldo a final de mes de una cuenta dada.
El saldo ya no es un atributo de la cuenta. Se obtiene recorriendo el historial mensual y anual que
registra el importe del saldo de la cuenta para cada mes.
3. Rehacer las definiciones anteriores.
Una tabla clientes contiene las cuentas corrientes de un conjunto de clientes.
4. Determinar los clientes para los que la media de los importes de los movimientos es superior a una suma dada.
El ejercicio siguiente se resolverá por completo en el capítulo «Edición de un número»."""
Cuentas = {}
Cuentas["Cuenta1"] = {"Nombre": "Juan", "Saldo": 1000, "Movimientos": [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]}
print(Cuentas)
def CrearCuenta (): # Esta funcion crea las cuentas
    while True: 
        continuar2 = input ("¿Desea crear una cuenta? ")
        if continuar2 == "No":
            break
        else:
            numeroCuenta = input ("Introduzca el numero de cuenta: ")
            nombre = input ("Introduzca el nombre del cliente: ")
            saldo = input ("Introduzca el saldo de la cuenta: ")
            movimientosTotales = []
            while True:
                movimientos = input ("Introduzca los movimientos de la cuenta: ")
                movimientosTotales.append(movimientos)
                continuar = input ("¿Desea introducir otro movimiento?: ")
                if continuar == "No":
                    break
                else:
                    continue
            Cuentas[numeroCuenta] = {"Nombre": nombre, "Saldo": saldo, "Movimientos": movimientosTotales}
        print(Cuentas)