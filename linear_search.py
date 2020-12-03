def linear_search(A, v):
	"""returns the index of value v in A or None if v is not in A.

	Correctness:
	Loop invariant: At the start of each iteration of the for loop,
	the subarray A[0..index] consists of elements that do not include v


	Example Usage:

	>>> linear_search([5, 3, 4, 2, 6, 1], 4)
	2
	>>> linear_search([5, 4, 3, 2, 6, 1], 7) is None
	True
	"""
	for index, item in enumerate(A):

		if item == v:
			return index

	return None

if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True,
					optionflags=doctest.NORMALIZE_WHITESPACE)