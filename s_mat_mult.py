import random

def sq_mat(n, k):
	sq_mat = []
	for i in range(n):
		sq_mat.append(random.sample(list(range(k)), n))
	return sq_mat


def sq_mat_mult(A, B):
	n = len(A)
	C = [[0]*n for _ in range(n)]

	for i in range(n):
		for j in range(n):
			# C[i][j] is initialized with a value of 0
			for k in range(n):
				C[i][j] += A[i][k]*B[k][j]
				
	return C






if __name__ == '__main__':
	n = 2
	k = 10

	A = sq_mat(n, k)
	B = sq_mat(n, k)

	print("A:")
	print(A[0])
	print(A[1])
	
	print("B:")
	print(B[0])
	print(B[1])


	C = sq_mat_mult(A, B)

	print("C:")
	print(C[0])
	print(C[1])