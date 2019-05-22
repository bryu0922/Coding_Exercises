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

	def node1(self):
		return self.node1_

	def node2(self):
		return self.node2_

	def weight(self):
		return self.weight_

class Graph:
	def __init__(self): #Works
		self.nodes_ = []
		self.edges_ = []
		return

	def size(self): #Works
		return len(self.nodes_)

	def num_nodes(self): #Works
		return self.size()

	def add_node(self, value): #Works
		newNode = Node(value, len(self.nodes_), self)
		self.nodes_.append(newNode)
		return

	def has_node(self, node): #Works
		return node.homeGraph_ == self

	def node(self, idx): #Works
		if idx >= len(self.nodes_):
			return None
		return self.nodes_[idx]

	def edge(self, idx): #Works
		if idx > self.num_edges():
			return None
		currentSum = 0
		for i in range(len(self.edges_)):
			toAdd = len(self.edges_[i])
			if currentSum + toAdd > idx:
				return self.edges_[i][idx - (currentSum + toAdd)]
			else:
				currentSum += toAdd
		return None

	def num_edges(self): #Works
		totalEdges = 0
		for i in range(len(self.edges_)):
			totalEdges += len(self.edges_[i])
		return int(totalEdges/2)

	def has_edge(self, node1, node2): #Works
		n1_idx = node1.index()
		n2_idx = node2.index()

		for i in range(len(self.edges_)):
			# For each node
			currList = self.edges_[i]

			for j in range(len(currList)):
				if ((self.edges_[i][j]).node1().index() ==  n1_idx and self.edges_[i][j].node2().index() == n2_idx) or (self.edges_[i][j].node1().index() ==  n2_idx and self.edges_[i][j].node2().index() == n1_idx):
					return True

		return False

	def add_edge(self, node1, node2, weight = None): #Works
		if (self.has_edge(node1, node2)):
			return
		# Edge does not exist
		n1_idx = node1.index()
		n2_idx = node2.index()

		while len(self.edges_) <= n1_idx:
			self.edges_.append([])
		while len(self.edges_) <= n2_idx:
			self.edges_.append([])

		currEdge1 = Edge(node1, node2, weight)
		currEdge2 = Edge(node2, node1, weight)

		self.edges_[n1_idx].append(currEdge1)
		self.edges_[n2_idx].append(currEdge2)
		

		return

	def clear(): #Works
		del self.nodes_
		del self.edges_
		self.nodes_ = []
		self.edges_ = []
		return


g = Graph()
print("Num Nodes: " + str(g.num_nodes()))
g.add_node(5)
g.add_node(7)
g.add_node(2)
g.add_node(8)
g.add_node(1)
g.add_node(4)


print("Num Nodes: " + str(g.size()))
print(g.node(1))

g.add_edge(g.node(0), g.node(3))
print((g.edges_))
g.add_edge(g.node(1), g.node(3))
g.add_edge(g.node(2), g.node(3))
print((g.num_edges()))
print((g.edges_))
print(g.edge(10))