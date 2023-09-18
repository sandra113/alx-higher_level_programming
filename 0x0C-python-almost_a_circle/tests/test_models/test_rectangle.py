import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_area(self):
        rectangle = Rectangle(4, 5)
        self.assertEqual(rectangle.area(), 20)

    def test_str_representation(self):
        rectangle = Rectangle(3, 7, 1, 2, 42)
        expected_str = "[Rectangle] (42) 1/2 - 3/7"
        self.assertEqual(str(rectangle), expected_str)

    # Add more test cases as needed...

if __name__ == '__main__':
    unittest.main()
