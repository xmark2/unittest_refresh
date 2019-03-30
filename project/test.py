import unittest

from my_sum import sum
from my_avg import avg


class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 2, "sum failed")


class TestAvg(unittest.TestCase):
	def test_list_avg_init(self):
		data_avg = [1,2,3]
		result = avg(data_avg)
		self.assertEqual(result, 3, "avg failed")


if __name__ == '__main__':
    unittest.main()