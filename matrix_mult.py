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
	n = len(A)
	C = [[0]*n]*n

	# A = [[0, 1] [0, 1]]    a11 a12    b11 b12
	# B = [[2, 1] [2, 3]]    a21 a22    b21 b22
	
	# c11 = a11*b11 + a12*b21
	# c21 = a21*b11 + a22*b21
	# c12 = a11*b12 * a12*b22
	# c22 = a21*b12 + a12*b22

	for i in range(len(A)):
		c_ij = 0
		# for j in range(len(B[0])):
			# print(A[i]d[j], B[j][i])
			# c_ij *= A[i][j] + B[j][i]
		# print(c_ij)
		# C[i][j] = c_ij
	return C

if __name__ == '__main__':
	# A = make_matrix(2) # 2x2 matrix
	# B = make_matrix(2) # 2x2 matrix
	A = [[0, 1], [0, 1]]
	B = [[2, 1], [2, 3]]

	print("A:", A)
	print("B:", B)
	C = sq_matrix_mult(A, B)
	print("C:", C)