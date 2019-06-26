import unittest
from fields import rectangle


class RectangleTestCase(unittest.TestCase):
    def setUp(self):
        self.a = 10
        self.b = 50

    def test_rectangle_with_correct_values(self):
        self.assertEqual(rectangle(self.a, self.b), 500)

    def tearDown(self):
        del self.a
        del self.b



if __name__ == '__main__':
    unittest.main()
