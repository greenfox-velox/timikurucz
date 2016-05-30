import unittest
import extend

class TestExtend(unittest.TestCase):
    def setUp(self):
        pass
    def test_add_2_and_3_is_5(self):
        self.assertEqual(extend.add(2, 3), 5)
    def test_add_2_and_4_is_6(self):
        self.assertEqual(extend.add(2, 4), 6)

    def test_max_of_three_first(self):
        self.assertEqual(extend.max_of_three(5, 4, 3), 5)
    def test_max_of_three_same_numbers(self):
        self.assertEqual(extend.max_of_three(-21,-21,-21),-21)

    def test_median_four(self):
        self.assertEqual(extend.median([7,5,3,5]), 5)
    def test_median_five(self):
        self.assertEqual(extend.median([1,2,3,4,5]), 3)

    def test_is_vovel_a(self):
        self.assertTrue(extend.is_vovel('a'))
    def test_is_vovel_b(self):
        self.assertFalse(extend.is_vovel('b'))
    def test_is_vovel_A(self):
        self.assertTrue(extend.is_vovel('A'))

    def test_translate_bemutatkozik(self):
        self.assertEqual(extend.translate('bemutatkozik'), 'bevemuvutavatkovozivik')
    def test_translate_kolbice(self):
        self.assertEqual(extend.translate('koala'), 'kovoavalava')

if __name__ == '__main__':
    unittest.main()
