import math
import sys

def max_subarray(A):
	"""return the maximum subarray of A, the nonempty contiguous 
	subarray of A whose values have the largest sum
	brute force: try every pair of dates 
	where the sell date is after the buy date

	Args:

		A - list - list of integers
	"""
	
	max_sum = 0
	best_buy_date = 0
	best_sell_date = 0
	for buy_date in range(len(A)):
		for sell_date in range(buy_date, len(A)):
			if sum(A[buy_date:sell_date]) > max_sum:
				max_sum = sum(A[buy_date:sell_date])
				best_buy_date = buy_date
				best_sell_date = sell_date

	return A[best_buy_date: best_sell_date], max_sum

def max_crossing_subarray(A, low, mid, high):
	"""return sum and indices of a maximum subarray that crosses the middle of A, e.g., 
	A[i..mid], A[mid+1..j], where low <= i <= mid <= j <= high
	
	Args:

		A - list - list of integers
		low - int - index of first element
		mid - int - index of middle index (floor((low + high) / 2))
		high - int - index of last element
	"""

	left_sum = -(sys.maxsize)
	crossing_sum = 0
	min_left = 0

	for left_i in range(mid, low - 1, -1):
		crossing_sum += A[left_i]

		if crossing_sum > left_sum:
			left_sum = crossing_sum
			min_left = left_i

	right_sum = -(sys.maxsize)
	crossing_sum = 0
	max_right = 0

	for right_j in range(mid + 1, high):
		crossing_sum += A[right_j]

		if crossing_sum > right_sum:
			right_sum = crossing_sum
			max_right = right_j

	return min_left, max_right, left_sum + right_sum

def find_maximum_subarray(A, low, high):
	"""return sum and indices of a maximum subarray of A, a nonempty contiguous 
	subarray of A whose values have the largest sum
	divide and conquer: find max left subarray, max right subarray, and max crossing subarray

	Args:

		A - list - list of integers
		low - int - index of first element
		high - int - index of last element
	"""

	# Base case: one element in A
	if high == low:
		return (low, high, A[low])

	mid = math.floor((low + high) / 2)
	
	# Recursively find max subarray on Left
	left_low, left_high, left_sum = find_maximum_subarray(A, low, mid)

	# Recursively find max subarray on Right
	right_low, right_high, right_sum = find_maximum_subarray(A, mid + 1, high)

	# Find max Crossing subarray
	cross_low, cross_high, cross_sum = max_crossing_subarray(A, low, mid, high)

	# Max on left:
	if left_sum >= right_sum and left_sum >= cross_sum:
		return left_low, left_high, left_sum

	# Max on right:
	if right_sum >= left_sum and right_sum >= cross_sum:
		return right_low, right_high, right_sum

	return cross_low, cross_high, cross_sum



if __name__ == '__main__':
	
	A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
	
	low = 0
	high = len(A) - 1

	print(find_maximum_subarray(A, low, high))
	

