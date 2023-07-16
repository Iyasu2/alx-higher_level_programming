import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_init(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base(12)
        self.assertEqual(b3.id, 12)

        b4 = Base()
        self.assertEqual(b4.id, 3)

    def test_to_json_string(self):
        c1 = Base()
        c_dict = c1.to_dictionary()
        json_dict = Base.to_json_string([c_dict])
        self.assertEqual(json_dict, '[{"id": 5}]')

    def test_from_json_string(self):
        json_dict = '[{"id": 1}]'
        list_dicts = Base.from_json_string(json_dict)
        self.assertEqual(list_dicts, [{"id": 1}])

    def test_save_to_file(self):
        d1 = Base()
        d2 = Base(45)
        list_objs = [d1, d2]
        Base.save_to_file(list_objs)
        with open("Base.json", mode="r", encoding="utf=8") as f:
                self.assertEqual(f.read(), '[{"id": 4}, {"id": 45}]')
