import copy
import random
import time

'''
Partial Sort Select
Author: Brian K. Ryu
Time complexity: O(kN)

Find k-th smallest element by finding all the 1,2,...,k-th smallest element
'''
def partialSortSelect(arr, k):
	# First take the length of array
	N = len(arr)
	arrCpy = copy.deepcopy(arr)
	
	# For first k smallest element
	for i in range(k):
		currMinVal = arrCpy[i]
		currMinIdx = i

		#Find minimum
		for j in range(i,N):
			if arrCpy[j] < currMinVal:
				currMinVal = arrCpy[j]
				currMinIdx = j
		arrCpy[i], arrCpy[currMinIdx] = arrCpy[currMinIdx],  arrCpy[i]

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
	print('k-th smallest = ' + str(partialSortSelect(testArr, k)))

	print("Sorted array is: ")
	testArr.sort()
	print(testArr)

testRun()