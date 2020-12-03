def insertion_sort(sequence, increasing=True):
	"""Sort the n keys in the sequence in-place using insertion sort.
	Defaults to sorting in non-decreasing order.
	Setting inc=False sorts in non-increasing order.

	Example usage:

	>>> insertion_sort([2, 5, 4, 3, 1, 6])
	[1, 2, 3, 4, 5, 6]
	>>> insertion_sort([5, 2, 4, 6, 1, 3], increasing=False)
	[6, 5, 4, 3, 2, 1]
	"""

	for key_index in range(1, len(sequence)):
		
		key = sequence[key_index]

		test_index = key_index - 1

		if increasing:
			while test_index > -1 and sequence[test_index] > key:
				sequence[test_index + 1] = sequence[test_index]
				test_index -= 1
		else:
			while test_index > -1 and sequence[test_index] < key:
				sequence[test_index + 1] = sequence[test_index]
				test_index -= 1

		sequence[test_index + 1] = key

	return sequence


if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True,
					optionflags=doctest.NORMALIZE_WHITESPACE)