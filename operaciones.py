def sumar (a, b): # define una función para sumar dos números
    return a+b

def restar(a, b): # define una función para restar dos números
    return a - b

def multiplicar(a, b): # define una función para multiplicar dos números
    return a * b

def dividir(a, b): # define una función para dividir dos números
    if b == 0: # comprueba si el segundo valor es 0
        raise ValueError("No se puede dividir por cero") # llamada a excepcion ValueError
    return a / b

if __name__ == "__main__":
    print(sumar(5, 6))
    print(restar(10,4))
    print(multiplicar(3,2))
    print(dividir(10,2))
