import random
import time
'''
Bogo Sort
Time complexity: O(N * (N!))

Inputing visualize = True as a second argument prints out array at
every outer loop iteration.

'''
def isSorted(arr):
	N = len(arr)

	for i in range(N-1):
		if arr[i] > arr[i+1]:
			return False

	return True
def BogoSort(arr, visualize=False):
	counter = 0

	while True:	
		counter += 1
		if (visualize):
				print(arr)

		random.shuffle(arr)

		if isSorted(arr):
			break
	if (visualize):
		print(arr)
	print("Number of shuffles: " + str(counter))



def testRun():
	random.seed(time.time())
	testN = 5

	testArr = [0]*testN

	for i in range(testN):
		testArr[i] = random.randrange(100)

	BogoSort(testArr, True)



testRun()