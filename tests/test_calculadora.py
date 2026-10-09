
import unittest
from calculadora import sumar, restar, multiplicar, dividir


class TestCalculadora(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(sumar(10, 5), 15)

    def test_resta(self):
        self.assertEqual(restar(10, 5), 5)

    def test_multiplicacion(self):
        self.assertEqual(multiplicar(10, 5), 50)

    def test_division(self):
        self.assertEqual(dividir(10, 5), 2)

    def test_division_cero(self):
        with self.assertRaises(ValueError):
            dividir(10, 0)

    def test_numeros_negativos(self):
        self.assertEqual(sumar(-5, -3), -8)


if __name__ == "__main__":
    unittest.main()
