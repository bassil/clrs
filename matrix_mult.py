import random

def make_matrix(n):
	"""returns n by n matrix with elements selected from [0..n*2]"""
	matrix = []
	population = list(range(n*2))
	for i in range(n):
		matrix.append(random.sample(population, n))
	return matrix

def sq_matrix_mult(A, B):
	"""returns matrix product of square matrices A and B"""
	C = []
	# [0, 1] [0, 1]
	# [2, 1] [2, 3]
	# c11 = a11*b11 + a12*b21
	return C

if __name__ == '__main__':
	A = make_matrix(2) # 2x2 matrix
	B = make_matrix(2) # 2x2 matrix

	print("A:", A)
	print("B:", B)
	C = sq_matrix_mult(A, B)
	print("C:", C)