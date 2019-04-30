#include <algorithm>
#include <iostream>
#include <random>
#include <string>
#include <vector>

#include <stdlib.h>
#include <time.h>
/* BubbleSort
 * Time complexity: O(N^2)
 */
template<typename T>
void bubbleSort(std::vector<T> &vec) {
	// First take the length of array
	uint N = vec.size();

	//Outer loop. After i-th outer iteration, the last i elements are sorted
	for (uint i = 0 ; i < N; i++) {
		// Inner Loop
		for (uint j = 1; j < (N-i); j++) {
			if (vec[j-1] > vec[j]) {
				std::swap(vec[j-1], vec[j]);
			}
		}

	}
}

template<typename T>
void print(std::vector<T> vec) {
	std::cout<<"[";
	for (uint i = 0 ; i < vec.size(); i++) {
		std::cout<<vec[i]<<" ";
	}
	std::cout<<"]"<<std::endl;
	return;
}

void testRun() {
	int testN = 10;
	std::vector<int> testArr(testN);

	for (uint i = 0 ; i < testArr.size(); i++) {
		testArr[i] = i;
	}

	std::random_shuffle(testArr.begin(), testArr.end());
	print(testArr);
	bubbleSort(testArr);
	print(testArr);
	
}

int main() {

	testRun();
	return 0;
}