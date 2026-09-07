import math
import unittest

from reliability import calculate_reliability


class TestReliability(unittest.TestCase):
    def test_known_value(self):
        result = calculate_reliability(0.001, 100)
        self.assertAlmostEqual(result, math.exp(-0.1))

    def test_zero_time(self):
        self.assertEqual(calculate_reliability(0.001, 0), 1.0)

    def test_negative_time(self):
        with self.assertRaises(ValueError):
            calculate_reliability(0.001, -1)


if __name__ == "__main__":
    unittest.main()