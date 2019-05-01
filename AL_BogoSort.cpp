#include <algorithm>
#include <iostream>
#include <random>
#include <string>
#include <vector>

#include <stdlib.h>
#include <time.h>
/* BubbleSort
 * Time complexity: O(N * (N!))
 */
template<typename T>
bool isSorted(std::vector<T> &vec) {
	for (uint i = 1; i < vec.size(); i++) {
		if (vec[i] < vec[i-1]) {
			return false;
		}
	}
	return true;
}

template<typename T>
void bogoSort(std::vector<T> &vec) {
	uint counter = 0;
	while (isSorted(vec) == false) {
		std::random_shuffle(vec.begin(), vec.end());
		counter++;
	}
	std::cout<<"Sorted after " << counter << " shuffles!" << std::endl;
	return;

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

int myrandom (int i) { return std::rand()%i;}

void testRun() {
	int testN = 8;
	std::vector<int> testArr(testN);
	srand(time(0));

	for (uint i = 0 ; i < testArr.size(); i++) {
		testArr[i] = i;
	}

	std::random_shuffle(testArr.begin(), testArr.end(), myrandom);
	print(testArr);
	bogoSort(testArr);
	print(testArr);
	
}

int main() {

	testRun();
	return 0;
}