import unittest

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

class TestingMathMethods(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1,2), 3)
    def test_subtract(self):
        self.assertEqual(subtract(2, 1), 1)

if __name__ == "__main__":
    unittest.main()