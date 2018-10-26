import unittest

def running_sum(ls):
	'''Modify list so it contains the running sum of original elements'''
	for i in range(len(ls)):
		ls[i] = ls[i-1] + ls[i]

class TestRunningSum(unittest.TestCase):
	'''Tests for running_sum'''

	def test_running_sum_empty(self):
		'''Testing an empty list'''
		argument = []
		expected = []
		running_sum(argument)
		self.assertEqual(expected, argument,'The list is empty.')

	def test_running_sum_one(self):
		'''Tests a one-item list'''
		argument = [2]
		expected = [2]
		running_sum(argument)
		self.assertEqual(expected, argument, "The list contains one element.")

	def test_running_sum_two(self):
		'''Tests two-item list'''
		argument = [2,5]
		expected = [2,7]
		running_sum(argument)
		self.assertEqual(expected, argument, "The list contains two items.")

	def test_running_sum_multi_neg(self):
		'''Tests a list of negative values'''
		argument = [-1, -5, -3, -4]
		expected = [-1, -6, -9, -13]
		running_sum(argument)
		self.assertEqual(expected, argument, 'The list constains only negative values.')

	def test_running_sum_multi_zeros(self):
		'''Tests a list of zeros'''
		argument = [0,0,0,0]
		expected = [0,0,0,0]
		running_sum(argument)
		self.assertEqual(expected, argument, 'The list contains only zeros')

	def test_running_sum_multi_pos(self):
		'''Tests a list of positive values'''
		argument = [4, 0, 2, -5]
		expected = [4, 4, 6, 1]
		running_sum(argument)
		self.assertEqual(expected,argument, "The list constains zeros and positive and negative values.")

if __name__ == '__main__':
	unittest.main(argv=['first-arg-is-ignored'], exit=False)
