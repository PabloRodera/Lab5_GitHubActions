def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero.")
    return a / b

if __name__ == "__main__":
    print("Suma:", sumar(5, 3))
    print("Resta:", restar(5, 3))
    print("Multiplicación:", multiplicar(5, 3))
    try:
        print("División:", dividir(5, 3))
    except ValueError as e:
        print("Error:", e)