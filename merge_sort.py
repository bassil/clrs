import math
import random
import sys

from utils import timeit

def get_random_sequence(n, k):
	"""return a len n random sequence with max value k

	Args:

	n - int
		length of random sequence
	k - int
		upper bound for values of elements of the random sequence
	"""
	return random.sample(range(1, k), n)

def merge(A, p, q, r):
	"""From clrs: Auxillary function for merge_sort,
	p <= q < r

	Assuming subarrays A[p..q] and A[q+1..r] are sorted, 
	merge them to form a single sorted subarray

	Example Usage:
	>>> merge([1, 3, 5, 7, 9, 0, 2, 4, 6, 8], p=0, q=4, r=9)
	[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
	"""
	left = A[p : q + 1]
	
	right = A[q + 1 : r + 1]

	left_index = right_index = 0
	
	A_index = p
	
	# Proceed through the indices of the sequence
	# add the smaller of the two 
	while left_index < len(left) and right_index < len(right):

		if left[left_index] <= right[right_index]:

			A[A_index] = left[left_index]
			left_index += 1

		else:

			A[A_index] = right[right_index]
			right_index += 1

		A_index += 1

	if right_index == len(right):
		A[A_index : r + 1] = left[left_index : ]
	
	return A
	
def merge_sort(A, p, r):
	"""return A sorted using merge sort

	Example Usage:

	>>> merge_sort([5, 3, 6, 2, 1, 4])
	[1, 2, 3, 4, 5, 6]
	"""
	if p < r:
		q = math.floor((p + r)/2)

		merge_sort(A, p, q)
		
		merge_sort(A, q + 1, r)
		
		merge(A, p, q, r)

	return A

if __name__ == "__main__":
	# import doctest
	# doctest.testmod(verbose=True)
	n = 50000
	k = 100000
	sequence = get_random_sequence(n, k)
	
	# sequence = [1, 3, 5, 7, 9, 0, 2, 4, 6, 8]

	p = 0
	r = len(sequence) - 1
	
	with timeit("merge_sort on input size n = {}".format(n)):
		sorted_sequence = merge_sort(sequence, p, r)

