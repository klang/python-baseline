from sample import sum, sum_only_positive
import unittest


class TestSample(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum(5, 5), 10)

    def test_sum_positive_ok(self):
        self.assertEqual(sum_only_positive(2, 2), 4)

    def test_sum_positive_fail(self):
        self.assertIsNone(sum_only_positive(-1, 2))


# adding these two lines, will reduce cover to 90% when run from inside IntelliJ, but increase it to 100% when run from
# the command line.
if __name__ == "__main__":
    unittest.main()
