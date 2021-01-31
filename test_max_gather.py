import unittest
import max_gather


class TestMaxGather(unittest.TestCase):
    def test_get_max_apples(self):
        self.assertEqual(max_gather.get_max_apples([4, 5, 6, 1], 1, 2), (15, 2, 0))
        self.assertEqual(max_gather.get_max_apples([10, 20, 30, 40, 50, 60, 10], 2, 3), (200, 4, 1))
        self.assertEqual(max_gather.get_max_apples([1, 2, 3, 4], 2, 1), (9, 2, 1))

    def test_gather_order(self):
        returned = max_gather.get_max_apples([3, 4, 1, 7, 8, 5], 2, 3)
        gather_order = returned[1], returned[2]
        self.assertEqual(gather_order, (0, 3))

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
