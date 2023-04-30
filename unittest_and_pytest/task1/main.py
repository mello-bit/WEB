import unittest
from yandex_testing_lesson import reverse


class TestReverse(unittest.TestCase):
    def test_es(self):
        self.assertEqual(reverse(''), '')

    def test_oneCharS(self):
        self.assertEqual(reverse('t'), 't')

    def test_goodS(self):
        self.assertEqual(reverse('goog'), 'goog')

    def test_noGoodS(self):
        self.assertEqual(reverse('ell'), 'lle')

    def test_noS(self):
        with self.assertRaises(TypeError):
            reverse(905)

    def test_otherNoS(self):
        with self.assertRaises(TypeError):
            reverse([11, 32, 60])


if __name__ == '__main__':
    unittest.main()
