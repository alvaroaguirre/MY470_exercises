# Alvaro Aguirre
# MY470 Week 7 - Exercise 1 - Leading module

def leading_substrings(s):
	'''Takes string s as input and returns a list of 
	all substrings that start from the beginning.
	E.g. leading_substring('bear') -> ['b','be','bea','bear']'''
	return [s[:i+1] for i in range(len(s))]