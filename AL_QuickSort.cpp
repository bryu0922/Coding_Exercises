#include <algorithm>
#include <iostream>
#include <random>
#include <string>
#include <vector>

#include <stdlib.h>
#include <time.h>
/* QuickSort
 * Time complexity: O(N*logN)
 *
 * Includes a print function to visualize, and two helper functions
 * partition: Partitions array based on a pivot. Pivot is the first element of vector
 * quickSortPart: A method that runs quicksort in each recursive call
 */
template<typename T>
void print(std::vector<T> vec) {
	std::cout<<"[";
	for (uint i = 0 ; i < vec.size(); i++) {
		std::cout<<vec[i]<<" ";
	}
	std::cout<<"]"<<std::endl;
	return;
}

template<typename T>
uint partition(std::vector<T> &vec, uint lowIdx, uint highIdx) {
	T pivot = vec[lowIdx];
	uint smallIdx = lowIdx;

	for (uint i = lowIdx + 1 ; i < highIdx; i++) {
		if (vec[i] < pivot) {
			smallIdx++;
			std::swap(vec[smallIdx], vec[i]);
		} 

	}
	std::swap(vec[lowIdx], vec[smallIdx]);
	return smallIdx;
}

template<typename T>
void quickSortPart(std::vector<T> &vec, uint lowIdx, uint highIdx) {
	// First take the length of array
	uint N = highIdx - lowIdx;
	if (N <= 1) {
		return;
	}

	uint pivotLocation = partition(vec, lowIdx, highIdx);
	quickSortPart(vec, lowIdx, pivotLocation);
	quickSortPart(vec, pivotLocation+1, highIdx);
	return;
}


template<typename T>
void quickSort(std::vector<T> &vec) {
	// First take the length of array
	uint N = vec.size();
	if (N <= 1) {
		return;
	}
	quickSortPart(vec, 0, N);
	return;
}


int myrandom (int i) { return std::rand()%i;}

void testRun() {
	int testN = 12;
	std::vector<int> testArr(testN);
	srand(time(0));

	for (uint i = 0 ; i < testArr.size(); i++) {
		testArr[i] = i;
	}

	std::random_shuffle(testArr.begin(), testArr.end(), myrandom);
	print(testArr);
	quickSort(testArr);
	print(testArr);
	
}

int main() {
	testRun();
	return 0;
}