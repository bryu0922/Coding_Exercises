'''
Basic Linked List Class

Supported Methods:
	at(idx): Index access. Complexity: O(idx)
	delete(value): Delete a node by value. Complexity: O(N)
	insert(value): Insert a node to the front of linked list. Complexity: O(1)
	print(): Basic printing. Complexity: O(N)
	search(value): Search node by value. Complexity: O(N)
	size(): Print the number of nodes in this linked list. Complexity: O(N)

'''
class Node:
	def __init__(self, value=None, nextNode=None):
		self.value_ = None
		self.next_ = None

		if (value != None):
			self.value_ = value

		if (nextNode != None):
			self.next_ = nextNode


	def setData(self, value):
		self.value_ = value

	def getData(self):
		return self.value_

	def setNext(self, nextNode):
		self.next_ = nextNode

	def getNext(self):
		return self.next_


class LinkedList:
	def __init__(self, head=None):
		self.head_ = None

		if (head != None):
			self.head_ = head

	def at(self, idx):
		if (idx < 0):
			return None

		currNode = self.head_
		counter = 0
		while (counter < idx):
			currNode = currNode.getNext()
			counter += 1
		return currNode

	def delete(self, value):
		currNode = self.head_
		prevNode = None
		foundTarget = False

		while (currNode != None):
			if (currNode.getData() == value):
				# Found it!
				prevNode.setNext(currNode.getNext())
				break
			prevNode = currNode
			currNode = currNode.getNext()

	def insert(self, value):
		newNode = Node(value, self.head_)
		self.head_ = newNode

	def print(self):
		currNode = self.head_
		toPrint = "["
		while (currNode != None):
			toPrint += str(currNode.getData())
			toPrint += " "
			currNode = currNode.getNext()
		toPrint += "]"
		print(toPrint)

	def search(self, value):
		currNode = self.head_

		while (currNode != None):
			if (currNode.getData() == value):
				return currNode
			currNode = currNode.getNext()

	def size(self):
		currNode = self.head_

		counter = 0;
		while (currNode != None):
			currNode = currNode.getNext()
			counter += 1

		return counter


A = LinkedList()
print(A.size())
A.insert(5)
A.insert(3)
A.insert(0.5)
A.insert(0.7)
A.insert(0.1)
A.insert(0.4)
print(A.size())
print(A.search(0.5).getData())
A.print()
A.delete(0.5)
print(A.size())
A.print()
print(A.at(2).getData())