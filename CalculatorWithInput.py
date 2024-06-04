# Calculator with input
# Funktion für Rechnung
def calculator(num1, op, num2):
    # Variabel mit Wert 0 um mit zu arbeiten
    result = 0

    # Possible calculations:
    # Addieren
    if op == "+":
        result = num1 + num2

    # Subtrahieren
    elif op == "-":
        result = num1 - num2

    # Multiplizieren
    elif op == "*":
        result = num1 * num2

    # Dividieren
    elif op == "/":
        result = num1 / num2

    # Hoch rechnen / sqaured
    elif op == "**":
        result = num1 ** num2

    # Modulo (den Rest einer Division)
    elif op == "%":
        result = num1 % num2

    # wie oft die Zahl in zu teilende Zahl „komplett rein geht"
    elif op == "//":
        result = num1 // num2

        # Mögliche Operatoren Errors

    # If operator is nicht gültig.
    elif op != str:
        raise SyntaxError(" \n \n \n \n" "\x1B[4m" + "                 WARNING:                 " +
                          "\x1B[0m" "\n Please reload and enter a valid operator.")

    # falls op größer als 1
    elif len(op) < 1:
        raise SyntaxError("please enter a operator.")

    # falls op größer als 2
    elif len(op) > 2:
        raise SyntaxError("please enter a valid operator.")

    # Die Formel anzeigen
    print(f"{num1} {op} {num2} = {result}")


# Die Funktion rufen.
calculator(
    num1=int(input("Please enter first number: ")),
    op=str(input("Please enter the operator: ")),
    num2=int(input("Please enter the second number: "))
)

again = str(input("Do you want to do one more calculatrion?   Yes  | No"))
while again == true:
    def calculator(num1, op, num2):
        # Variabel mit Wert 0 um mit zu arbeiten
    result = 0

    # Possible calculations:
    # Addieren
    if op == "+":
        result = num1 + num2

    # Subtrahieren
    elif op == "-":
        result = num1 - num2

    # Multiplizieren
    elif op == "*":
        result = num1 * num2

    # Dividieren
    elif op == "/":
        result = num1 / num2

    # Hoch rechnen / sqaured
    elif op == "**":
        result = num1 ** num2

    # Modulo (den Rest einer Division)
    elif op == "%":
        result = num1 % num2

    # wie oft die Zahl in zu teilende Zahl „komplett rein geht"
    elif op == "//":
        result = num1 // num2

        # Mögliche Operatoren Errors

    # If operator is nicht gültig.
    elif op != str:
        raise SyntaxError(" \n \n \n \n" "\x1B[4m" + "                 WARNING:                 " +
                          "\x1B[0m" "\n Please reload and enter a valid operator.")

    # falls op größer als 1
    elif len(op) < 1:
        raise SyntaxError("please enter a operator.")

    # falls op größer als 2
    elif len(op) > 2:
        raise SyntaxError("please enter a valid operator.")

    # Die Formel anzeigen
    print(f"{num1} {op} {num2} = {result}")

# Die Funktion rufen.
calculator(
    num1=int(input("Please enter first number: ")),
    op=str(input("Please enter the operator: ")),
    num2=int(input("Please enter the second number: "))
)
