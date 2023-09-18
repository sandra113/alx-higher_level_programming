import unittest
from models.rectangle import Rectangle
from models.square import Square

class TestBase(unittest.TestCase):
    def test_to_json_string(self):
        rectangle = Rectangle(1, 2, 3, 4, 5)
        square = Square(6, 7, 8, 9)
        
        # Test the to_json_string method on Rectangle and Square instances
        json_string_rectangle = Rectangle.to_json_string([rectangle.to_dictionary()])
        json_string_square = Square.to_json_string([square.to_dictionary()])
        
        self.assertEqual(json_string_rectangle, '[{"id": 5, "width": 1, "height": 2, "x": 3, "y": 4}]')
        self.assertEqual(json_string_square, '[{"id": 9, "size": 6, "x": 7, "y": 8}]')

if __name__ == '__main__':
    unittest.main()
