import unittest
from main import saludo 

class TestSaludo(unittest.TestCase):
    def test_saludo(self):
        self.assertEqual(saludo(), "Hola CD/CI prueba pipeline1")

if __name__ == "__main__":
    unittest.main()
