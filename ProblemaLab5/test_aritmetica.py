import unittest
from arimetica import sumar, restar, multiplicar, dividir

class TestAritmetica(unittest.TestCase):
    def test_sumar(self):
        self.assertEqual(sumar(3, 10), 13)
        self.assertEqual(sumar(-1, 1), 0)
        self.assertEqual(sumar(-1, -1), -2)

    def test_restar(self):
        self.assertEqual(restar(5, 3), 2)
        self.assertEqual(restar(1, 3), -2)
        self.assertEqual(restar(-1, -1), 0)
    
    def test_multiplicar(self):
        self.assertEqual(multiplicar(3, 2), 6)
        self.assertEqual(multiplicar(-1, 1), -1)
        self.assertEqual(multiplicar(-1, -1), 1)

    def test_dividir(self):
        self.assertEqual(dividir(8, 4), 2)
        self.assertEqual(dividir(9, 3), 3)
        self.assertEqual(dividir(-6, 3), -2)
        self.assertEqual(dividir(0, 5), 0)

        with self.assertRaises(ValueError):
            dividir(6, 0)

if __name__ == '__main__':
    unittest.main()