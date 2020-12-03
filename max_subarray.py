import sys

def max_subarray(A):
	"""return the maximum subarray of A, the nonempty contiguous 
	subarray of A whose values have the largest sum
	brute force: try every pair of dates 
	where the sell date is after the buy date
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
	"""return indices of a maximum subarray that crosses the middle of A, e.g., 
	A[i..mid], A[mid+1..j], where low <= i <= mid <= j <= high"""
	left_sum = -(sys.maxsize)
	crossing_sum = 0

	for left_i in range(mid, low, -1):
		todo


	return

if __name__ == '__main__':
	
	A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
	
	low = 0
	mid = len(A)//2
	high = len(A)

	max_crossing_subarray(A, low, mid, high)

