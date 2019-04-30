import random
import time
'''
Insertion Sort
Time complexity: O(N^2)

Inputing visualize = True as a second argument prints out array at
every outer loop iteration.

'''
def insertionSort(arr, visualize=False):
	# First take the length of array
	N = len(arr)

	# Outer loop. After i-th outer iteration, the first i elements are sorted
	for i in range(N):
		if (visualize):
			print(arr)

		currMin = arr[i]
		currMinIdx = i

		# Inner Loop
		for j in range(i+1, N):
			if arr[j] < currMin:
				currMin = arr[j]
				currMinIdx = j

		arr[i], arr[currMinIdx] = arr[currMinIdx], arr[i]
				

	if (visualize):
			print(arr)

def testRun():
	random.seed(time.time())
	testN = 10

	testArr = [0]*testN

	for i in range(testN):
		testArr[i] = random.randrange(100)

	insertionSort(testArr, True)


testRun()