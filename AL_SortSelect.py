import copy
import random
import time
import AL_MergeSort as ms

'''
Sort Select
Author: Brian K. Ryu
Time complexity: O(N*log(N))

Find k-th smallest element by finding all the 1,2,...,k-th smallest element

First perform a mergesort and then return value
'''
def sortSelect(arr, k):
	arrCpy = copy.deepcopy(arr)
	ms.mergeSort(arrCpy)
	
	return arrCpy[k-1]


def testRun():
	random.seed(time.time())
	testN = 10

	testArr = [0]*testN

	for i in range(testN):
		testArr[i] = random.randrange(100)

	
	print(testArr)
	k = 4
	print("k = " + str(k))
	print('k-th smallest = ' + str(sortSelect(testArr, k)))

	print("Sorted array is: ")
	testArr.sort()
	print(testArr)

testRun()