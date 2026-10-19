def calculo_calculadora(num1 : float, num2 : float):
    """
    Devolver las cuatro soluciones de las cuatro operaciones:
    - Suma
    - Resta
    - División
    - Multiplicación
    """
    suma = num1 + num2
    resta = num1 - num2
    division = num1 / num2
    multiplicacion = num1 * num2
    return suma, resta, division, multiplicacion

def main():
    numero1 = float(input("Introduce un número: "))
    numero2 = float(input("Introduce otro número: "))
    suma, resta, division, multiplicacion = calculo_calculadora(numero1, numero2)
    print(f"La suma es {suma}")
    print(f"La resta es {resta}")
    print(f"La división es {division}")
    print(f"La multiplicación es {multiplicacion}")

if __name__ == "__main__":
    main()