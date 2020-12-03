def binary_add(A, B):
	"""returns len (n+1) sum of len n binary arrays A and B

	Example Usage:

	>>> binary_add([1, 0], [1, 0])
	[1, 0, 0]

	>>> binary_add([1, 1, 0, 1, 0, 0, 1], [1, 0, 0, 0, 0, 1, 1])
	[1, 0, 1, 0, 1, 1, 0, 0]
	"""
	# add elements of A and B from end (e.g., n-1, n-2, ..., 0)
	assert len(A) == len(B)

	index = len(A) - 1
	carry = 0
	C = []

	while index > -1:

		if carry == 0:
			if A[index] == B[index] == 1:
				C.append(0)
				carry = 1
			elif A[index] == B[index] == 0:
				C.append(0)
				carry = 0
			else:
				C.append(1)
				carry = 0
		else:
			if A[index] == B[index] == 1:
				C.append(1)
				carry = 1
			elif A[index] == B[index] == 0:
				C.append(1)
				carry = 0
			else:
				C.append(0)
				carry = 1
		
		index -= 1
	C.append(carry)
	C.reverse()
	return C

if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True,
					optionflags=doctest.NORMALIZE_WHITESPACE)