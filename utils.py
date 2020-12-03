import time

from contextlib import contextmanager

@contextmanager
def timeit(msg=''):
	"""context manager for logging execution time"""
	start = time.perf_counter()
	try:
		yield
	finally:
		duration = time.perf_counter() - start
		if msg:
			if duration < 60:
				print("{0} ({1:.3f} seconds)".format(msg, duration))
			else:
				print("{0} ({1} minutes, {2:.3f} seconds)".format(msg,
																  duration // 60,
																  duration % 60))
