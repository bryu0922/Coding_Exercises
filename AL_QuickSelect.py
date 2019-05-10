import copy
import random
import time

'''
Quick Select (Linear Time Selection)
Author: Brian K. Ryu
Time complexity: O(N)

Find k-th smallest element by finding all the 1,2,...,k-th smallest element

Partition based, like quick sort.
'''

def partition(arr, lowIdx, highIdx):
	if (highIdx - lowIdx) <= 1:
		return lowIdx
	pivot = arr[lowIdx];
	smallIdx = lowIdx;

	for i in range(lowIdx+1, highIdx):
		if arr[i] < pivot:
			smallIdx += 1
			arr[i], arr[smallIdx] = arr[smallIdx], arr[i]
			

	arr[smallIdx], arr[lowIdx] = arr[lowIdx], arr[smallIdx]
	return smallIdx

def quickSelect(arr, k):
	arrCpy = copy.deepcopy(arr)
	lowIdx = 0
	highIdx = len(arr)
	# Now partition

	while True:
		returnIdx = partition(arrCpy, lowIdx, highIdx)
		if (returnIdx == (k-1)):
			break
		elif (returnIdx >= k):
			highIdx = returnIdx

		else:
			lowIdx = returnIdx+1

	return arrCpy[k-1]


def testRun():
	random.seed(time.time())
	testN = 15

	testArr = [0]*testN

	for i in range(testN):
		testArr[i] = random.randrange(100)

	
	print(testArr)
	k = 4
	print("k = " + str(k))
	print('k-th smallest = ' + str(quickSelect(testArr, k)))

	print("Sorted array is: ")
	testArr.sort()
	print(testArr)

testRun()