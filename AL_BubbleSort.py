import random
import time
'''
BubbleSort
Time complexity: O(N^2)

Inputing visualize = True as a second argument prints out array at
every outer loop iteration.

'''
def bubbleSort(arr, visualize=False):
	# First take the length of array
	N = len(arr)

	# Outer loop. After i-th outer iteration, the last i elements are sorted
	for i in range(N):
		# Inner Loop
		if (visualize):
			print(arr)
		for j in range(1, N-i):
			if arr[j-1] > arr[j]:
				arr[j-1], arr[j] = arr[j], arr[j-1]


def testRun():
	random.seed(time.time())
	testN = 10

	testArr = [0]*testN

	for i in range(testN):
		testArr[i] = random.randrange(100)

	bubbleSort(testArr, True)



testRun()