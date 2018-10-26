# Alvaro Aguirre
# MY470 Week 7 - Exercise 1 - Testing module
#bear -- b be bea bear
import unittest
import leading

class TestLeadingSubs(unittest.TestCase):
	'''Tests for leading_substrings.'''

	def test_leading_sub_empty(self):
		'''Tests empty string'''
		input = ''
		output_expected = []
		output = leading.leading_substrings(input)
		self.assertEqual(output_expected, output, 'No characters')

	def test_leading_sub_one(self):
		'''Tests for one character'''
		input = 'a'
		output_expected = ['a']
		output = leading.leading_substrings(input)
		self.assertEqual(output_expected, output, 'One character')

	def test_leading_sub_two(self):
		'''Tests for two characters'''
		input = 'hi'
		output_expected = ['h', 'hi']
		output = leading.leading_substrings(input)
		self.assertEqual(output_expected, output, 'Two characters')

	def test_leading_sub_extra_space(self):
		'''Tests for one extra space at the beginning'''
		input = ' test'
		output_expected = [' ', ' t', ' te', ' tes', ' test']
		output = leading.leading_substrings(input)
		self.assertEqual(output_expected, output, 'Space beginning')

	def test_leading_sub_double_extra_space(self):
		'''Tests for one extra space at the beginning and end'''
		input = ' test '
		output_expected = [' ', ' t', ' te', ' tes', ' test', ' test ']
		output = leading.leading_substrings(input)
		self.assertEqual(output_expected, output, 'Space beginning and end')

	def test_leading_sub_multi_word(self):
		'''Test for more than one word'''
		input = 'the test ran'
		output_expected = ['t', 'th', 'the', 'the ', 'the t', 'the te', 'the tes', 'the test', 'the test ', 'the test r', 'the test ra', 'the test ran']
		output = leading.leading_substrings(input)
		self.assertEqual(output_expected, output, 'Multiple words')

if __name__ == '__main__':
	unittest.main()