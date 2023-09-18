import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_create_instance_with_id(self):
        instance = Base(1)
        self.assertEqual(instance.id, 1)

    def test_create_instance_without_id(self):
        instance1 = Base()
        instance2 = Base()
        self.assertEqual(instance1.id, 1)
        self.assertEqual(instance2.id, 2)

    def test_to_json_string(self):
        instance = Base(1)
        json_string = Base.to_json_string([instance.to_dictionary()])
        self.assertEqual(json_string, '[{"id": 1}]')

if __name__ == '__main__':
    unittest.main()
