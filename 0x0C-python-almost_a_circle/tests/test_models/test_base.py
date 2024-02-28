import unittest
from models.base import Base

"""Test cases for the module, base"""


class test_base(unittest.TestCase):
    """Testing for base"""
    def test_create_instance(self):
        obj = Base()
        self.assertIsInstance(obj, Base)
    
    def test_create_instance_with_id(self):
        obj = Base(10)
        self.assertEqual(obj.id, 10)

    def test_create_multiple_instances(self):
        obj1 = Base()
        obj2 = Base()
        obj3 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)
        self.assertEqual(obj3.id, 3)

    def test_create_instance_with_non_integer_id(self):
        with self.assertRaises(TypeError):
            Base("string")

    def test_to_json_string_empty_list(self):
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_with_data(self):
        data = [{'id': 1, 'name': 'test'}, {'id': 2, 'name': 'test2'}]
        self.assertEqual(Base.to_json_string(data), '[{"id": 1, "name": "test"}, {"id": 2, "name": "test2"}]')

if __name__ == "__main__":
    unittest.main()
