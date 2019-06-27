import unittest
from wojownik import Wojownik, WojownikError


class TestWojownik(unittest.TestCase):
    def test_warrior_with_correct_life(self):
        w = Wojownik(30)
        self.assertEqual(w._zycie, 30)
        self.assertEqual(w._doswiadczenie, 0)

    def test_warrior_with_incorrect_life(self):
        with self.assertRaises(WojownikError):
            Wojownik(-100)

    def test_repr(self):
        w = Wojownik(30)
        expected = 'Wojownik: hp=30, exp=0'
        received = w.__repr__()

        self.assertEqual(expected, received)

    def test_marsz(self):
        w = Wojownik(30)
        w.maszeruj(1000)
        self.assertEqual(20.0, w._doswiadczenie)

if __name__ == '__main__':
    unittest.main()
