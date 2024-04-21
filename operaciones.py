def sumar (a, b):
    return a+b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero") #llamada a excepcion ValueError
    return a / b

if __name__ == "__main__":
    print(sumar(5, 6))
    print(restar(10,4))
    print(multiplicar(3,2))
    print(dividir(10,2))
