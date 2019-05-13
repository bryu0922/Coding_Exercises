import copy
'''
Basic Graph Class

Supported Methods:
	at(idx): Index access. Complexity: O(idx)
	delete(value): Delete a node by value. Complexity: O(N)
	insert(value): Insert a node to the front of linked list. Complexity: O(1)
	print(): Basic printing. Complexity: O(N)
	search(value): Search node by value. Complexity: O(N)
	size(): Print the number of nodes in this linked list. Complexity: O(N)

'''
class Node:
	def __init__(self, value=None, idx=None, homeGraph = None):
		self.value_ = value
		self.idx_ = idx
		self.homeGraph_ = homeGraph
		return

	def value(self):
		return self.value_


	def index(self):
		return self.idx_

class Edge:
	def __init__(self, node1, node2, weight=None):
		self.node1_ = node1
		self.node2_ = node2
		self.weight_ = weight
		return

	def node1():
		return self.node1_

	def node2():
		return self.node2_

	def weight():
		return self.weight_

class Graph:
	def __init__(self):
		self.nodes_ = []
		self.edges_ = []
		return

	def size(self):
		return len(self.nodes_)

	def num_nodes(self):
		return self.size()

	def add_node(self, value):
		newNode = Node(value, len(self.nodes_), self)
		self.nodes_.append(newNode)
		return

	def has_node(self, node):
		return node.homeGraph_ == self

	def node(self, idx):
		return self.nodes_[idx]

	def edge(self, idx):
		return self.edges_[idx]

	def has_edge(self, node1, node2):
		n1_idx = node1.index()
		n2_idx = node2.index()

		n1_neighbors = len(self.edges_[n1_idx])
		for i in range(n1_neighbors):
			currEdge = self.edges_[n1_idx][i]
			if currEdge.node2() == node2:
				return true

		n2_neighbors = len(self.edges_[n2_idx])
		for i in range(n2_neighbors):
			currEdge = self.edges_[n2_idx][i]
			if currEdge.node2() == node1:
				return true

		return

	def add_edge(self, node1, node2, weight = None):
		if (self.has_edge(node1, node2)):
			return
		# Edge does not exist
		n1_idx = node1.index()
		n2_idx = node2.index()

		while len(self.edges_) < n1_idx:
			self.edges_.append([])
		while len(self.edges_) < n2_idx:
			self.edges_.append([])

		currEdge1 = Edge(node1, node2, weight)
		currEdge2 = Edge(node2, node1, weight)

		

		return

	def clear():
		del self.nodes_
		del self.edges_
		self.nodes_ = []
		self.edges_ = []
		return


g = Graph()
print(g.num_nodes())
g.add_node(5)
print(g.num_nodes())
print(g.node(0).homeGraph_)
print(g.has_node(g.node(0)))

