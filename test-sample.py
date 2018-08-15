from sample import sum, sum_only_positive
import unittest


class TestSample(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum(5, 5), 10)

    def test_sum_positive_ok(self):
        self.assertEqual(sum_only_positive(2, 2), 4)

    def test_sum_positive_fail(self):
        self.assertIsNone(sum_only_positive(-1, 2))


if __name__ == "__main__":
    unittest.main()