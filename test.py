import unittest  # importa el módulo unittest

from operaciones import sumar, restar, multiplicar, dividir  # importa las funciones desde el módulo operaciones

class Test(unittest.TestCase):  # define una clase de prueba que hereda de unittest.TestCase

    def test_sumar(self):  # define un método de prueba para la función sumar
        self.assertEqual(sumar(3, 2), 5)  # comprueba si la suma de 3 y 2 es igual a 5
        self.assertEqual(sumar(-1, 1), 0)  # comprueba si la suma de -1 y 1 es igual a 0
        self.assertEqual(sumar(-1, -1), -2)  # comprueba si la suma de -1 y -1 es igual a -2

    def test_restar(self):  # define un método de prueba para la función restar
        self.assertEqual(restar(5, 3), 2)  # comprueba si la resta de 5 y 3 es igual a 2
        self.assertEqual(restar(-1, 1), -2)  # comprueba si la resta de -1 y 1 es igual a -2
        self.assertEqual(restar(-1, -1), 0)  # comprueba si la resta de -1 y -1 es igual a 0

    def test_multiplicar(self):  # define un método de prueba para la función multiplicar
        self.assertEqual(multiplicar(2, 3), 6)  # comprueba si el producto de 2 y 3 es igual a 6
        self.assertEqual(multiplicar(-1, 4), -4)  # comprueba si el producto de -1 y 4 es igual a -4
        self.assertEqual(multiplicar(-2, -2), 4)  # comprueba si el producto de -2 y -2 es igual a 4

    def test_dividir(self):  # define un método de prueba para la función dividir
        self.assertEqual(dividir(6, 3), 2)  # comprueba si la división de 6 entre 3 es igual a 2
        self.assertEqual(dividir(10, 2), 5)  # comprueba si la división de 10 entre 2 es igual a 5
        self.assertRaises(ValueError, dividir, 5, 0)  # comprueba si se llama a excepción ValueError al dividir por cero

if __name__ == "__main__":
    unittest.main()  # ejecuta las pruebas unitarias
