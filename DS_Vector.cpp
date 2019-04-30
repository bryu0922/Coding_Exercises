#include <algorithm>
#include <iostream>

/* Vector Class that mimics the STL class vector
 *
 * Available methods:
 *
 *  operator[](value): Index acess at position value
 *
 *  capacity(): returns capacity of vector
 *  empty(): True if vector is empty, false otherwise
 *  pop_back(): Deletes value at the back of the vector
 *  print(): Prints elements of vector (not in STL, but added for convenience)
 *  push_back(value): Both lvalue and rvalue implementations of insertion of value at end
 *  reserve(value): increase the capacity of vector to value
 *  resize(value): re-size the vector to value
 *  size(): returns size of vector.
 *
 *  begin(): Iterator to the first element (regular and constant implementations)
 *  end(): Iterator to one past the last element (regular and constant implementations)
 */
template<typename T>
class Vector {
    public: 
        /* Constructors and destructors */
        Vector(int inSize = 0) : vecCapacity{inSize + SPARE_CAPACITY}, vecSize{inSize}
            { values = new T[vecCapacity];}

        ~Vector() {
            delete[] values;
        }

        /* Operator Overloads */
        T& operator[] (int idx) {
            return values[idx];
        }

        const T& operator[] (int idx) const {
            return values[idx];
        }

        /* Public methods */
        int capacity() const {
            return vecCapacity;
        }

        bool empty() const {
            return (size() == 0);
        }

        void pop_back() {
            vecSize -= 1;
        }

        void print() {
            auto begItr = begin();
            auto endItr = end();

            std::cout << "[ ";
            for (; begItr != endItr; ++begItr) {
                std::cout << *begItr << " ";
            }
            std::cout << "]" << std::endl;
        }

        void push_back(T& val) {
            if (vecSize == vecCapacity) {
                reserve(vecCapacity*2);
            }
            values[vecSize] = val;
            vecSize += 1;
        }

        void push_back(T&& val) {
            if (vecSize == vecCapacity) {
                reserve(vecCapacity*2);
            }
            values[vecSize] = std::move(val);
            vecSize += 1;
        }

        void reserve(int inCapacity) {
            if (vecCapacity > inCapacity) {
                return;
            }
            
            T* newValues = new T[inCapacity];
            for (int i = 0 ; i < vecSize; i++) {
                newValues[i] = std::move(values[i]);
            }

            vecCapacity = inCapacity;
            std::swap(values, newValues);
            delete[] newValues;
        }

        void resize(int inSize) {
            if (inSize > vecCapacity) {
                reserve(inSize*2);
            }
            vecSize = inSize;
        }

        
        int size() const {
            return vecSize;
        }

        /* Iterator methods */
        T* begin() 
            { return &values[0]; }

        const T* begin() const
            { return &values[0]; }

        T* end() 
            { return &values[size()]; }

        const T* end() const 
            { return &values[size()]; }

    private:
        int SPARE_CAPACITY = 8;
        int vecCapacity;
        int vecSize;
        T* values;
};


int main() {

    Vector<double> vec;
    vec.push_back(7.2);
    vec.push_back(29.1);
    vec.push_back(582);
    vec.push_back(11.8);


    std::cout<<"Size of vector: " << vec.size() << std::endl;
    std::cout<<"Capacity of vector: " << vec.capacity() << std::endl;

    vec.print();
    

    return 0;
}