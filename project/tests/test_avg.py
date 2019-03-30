import unittest

from my_avg import avg

class TestAvg(unittest.TestCase):
	def test_list_avg_init(self):
		data_avg = [1,2,3]
		result = avg(data_avg)
		self.assertEqual(result, 2, "avg failed")


if __name__ == '__main__':
    unittest.main()