import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    def test_area(self):
        square = Square(4, 2, 3, 42)
        self.assertEqual(square.area(), 16)

    def test_str_representation(self):
        square = Square(5, 1, 1, 10)
        expected_str = "[Square] (10) 1/1 - 5"
        self.assertEqual(str(square), expected_str)

    # Add more test cases as needed...

if __name__ == '__main__':
    unittest.main()
