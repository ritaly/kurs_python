import unittest
from fields import rectangle, triangle, trapezoid


class FieldsTestCase(unittest.TestCase):
    def setUp(self):
        self.a = 10
        self.h = 50

    def test_rectangle_with_correct_values(self):
        self.assertEqual(rectangle(self.a, self.h), 500)

    def test_triangle_with_correct_values(self):
        self.assertEqual(triangle(self.a, self.h), 250)

    def test_trapezoid_with_correct_values(self):
        self.assertEqual(trapezoid(self.a, 5, self.h), 375)

    def tearDown(self):
        del self.a
        del self.h


if __name__ == '__main__':
    unittest.main()
