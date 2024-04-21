import unittest

from operaciones import sumar,restar, multiplicar, dividir

class TestSumar(unittest.TestCase):

    def test_sumar(self):
        self.assertEqual(sumar(3,2),5)
        self.assertEqual(sumar(-1,1),0)
        self.assertEqual(sumar(-1,-1),-2)


    def test_restar(self):
        self.assertEqual(restar(5, 3), 2)
        self.assertEqual(restar(-1, 1), -2)
        self.assertEqual(restar(-1, -1), 0)

    def test_multiplicar(self):
        self.assertEqual(multiplicar(2, 3), 6)
        self.assertEqual(multiplicar(-1, 4), -4)
        self.assertEqual(multiplicar(-2, -2), 4)

    def test_dividir(self):
        self.assertEqual(dividir(6, 3), 2)
        self.assertEqual(dividir(10, 2), 5)
        self.assertRaises(ValueError, dividir, 5, 0)

if __name__ == "__main__":
    unittest.main()