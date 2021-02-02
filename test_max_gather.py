import unittest
import max_gather


class TestMaxGather(unittest.TestCase):
    def test_get_max_apples(self):
        self.assertEqual(max_gather.get_max_apples([3, 4, 1, 7, 8, 5], 2, 3), (27, 0, 3))
        self.assertEqual(max_gather.get_max_apples([1, 3, 5], 2, 2), (-1, 0, 0))
        self.assertEqual(max_gather.get_max_apples([4, 5, 6, 1], 1, 2), (15, 0, 1))
        self.assertEqual(max_gather.get_max_apples([10, 20, 30, 40, 50, 60, 10], 2, 3), (200, 1, 3))
        self.assertEqual(max_gather.get_max_apples([1, 1, 5, 3, 2, 0], 2, 2), (11, 1, 3))
        self.assertEqual(max_gather.get_max_apples([1, 2, 3.5, 4], 2.1, 1.5), (9, 1, 3))
        self.assertEqual(max_gather.get_max_apples([1, 1, 6, 2, 0, 3, 20, 50], 2, 3), (81, 2, 5))
        self.assertEqual(max_gather.get_max_apples([50, 20, 3, 0, 2, 6, 1, 1], 2, 3), (81, 4, 0))

    def test_invalid_parameters(self):
        self.assertRaises(TypeError, max_gather.get_max_apples)
        self.assertRaises(TypeError, max_gather.get_max_apples, 2, 5, 6, 1)
        self.assertRaises(TypeError, max_gather.get_max_apples, [2, 5, 6], 1)

        self.assertRaises(ValueError, max_gather.get_max_apples, ['a1, 2'], 2, 2)
        self.assertRaises(ValueError, max_gather.get_max_apples, 'texto, teste', 2, 2)
        self.assertRaises(ValueError, max_gather.get_max_apples, 9, 2, 2)
        self.assertRaises(ValueError, max_gather.get_max_apples, True, 2, 2)


if __name__ == '__main__':
    unittest.main()
