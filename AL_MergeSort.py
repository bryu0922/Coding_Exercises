import math
import random
import time
'''
MergeSort
Time complexity: O(N*logN)

Merges in place

'''
def mergeSort(arr):
	# First take the length of array
	N = len(arr)
	halfIdx = N//2

	# halfIdx = math.ceil(N/2)

	if N < 2:
		return
	else:
		Left = arr[:halfIdx]
		Right = arr[halfIdx:]
		# Left Side
		mergeSort(Left)
		# Right Side
		mergeSort(Right)

		# Merge
		leftCount = 0
		rightCount = 0
		arrCount = 0

		while (leftCount < len(Left) and rightCount < len(Right)):
			if Left[leftCount] < Right[rightCount]:
				arr[arrCount] = Left[leftCount]
				leftCount += 1
			else:
				arr[arrCount] = Right[rightCount]
				rightCount += 1
			arrCount += 1

		# Either left or right may have finished first. Complete merging
		while leftCount < len(Left):
			arr[arrCount] = Left[leftCount]
			leftCount += 1
			arrCount += 1
		while rightCount < len(Right):
			arr[arrCount] = Right[rightCount]
			rightCount += 1
			arrCount += 1



def testRun():
	random.seed(time.time())
	testN = 20

	testArr = [0]*testN

	for i in range(testN):
		testArr[i] = random.randrange(100)

	print(testArr)
	mergeSort(testArr)
	print(testArr)

testRun()