from collections import deque

class Graph(object):			# implementation of undirected unweighted graphs

	def __init__(self):
		self.neighbours = []		# double list containing the names of the neighbours of a specific vertex
		self.name2index = {}		# dict that relates the name of a vertex to its index (between 0 and n-1)
		self.node_names = []		# list containing the names of all vertices of the graph
		self.seen = []				# useful list for searching algorithms


	def __len__(self):					# return the number of vertices of the graph
		return len(self.node_names)


	def __getitem__(self, v_name):			# return the neighbours of the vertex called v_name
		v_index = self.name2index[v_name]
		return self.neighbours[v_index]


	def degree(self, v_name):					# return the degree of the vertex called v_name
		return len(self.__getitem__(v_name))


	def add_node(self, v_name):								# add a new vertex
		assert v_name not in self.name2index
		self.name2index[v_name] = len(self.name2index)		# use len() to keep track of the index value (recall that they are from 0 to n-1)
		self.node_names.append(v_name)
		self.neighbours.append([])
		self.seen.append(False)
		# self.weights.append({})


	def add_edge(self, u_name, v_name, weights_uv=None):		# add a new edge between two nodes
		u_index = self.name2index[u_name]
		v_index = self.name2index[v_name]
		self.neighbours[u_index].append(v_name)
		self.neighbours[v_index].append(u_name)
		# self.weights[u_index][v_index] = weights_uv


	def bfs(self, start_name):									# Breadth-First-Search
		self.clear_labels()
		start_index = self.name2index[start_name]
		self.seen[start_index] = True
		to_visit = deque([start_name])
		output = [start_name]
		while to_visit:
			node = to_visit.pop()
			for neighbour in self.__getitem__(node):
				neighbour_index = self.name2index[neighbour]
				if not self.seen[neighbour_index]:
					self.seen[neighbour_index] = True
					output.append(neighbour)
					to_visit.appendleft(neighbour)
		return output


	def dfs(self, start_name):								# Dept-First-Search
		start_index = self.name2index[start_name]
		self.seen[start_index] = True
		output = [start_name]
		for neighbour in self.__getitem__(start_name):
			neighbour_index = self.name2index[neighbour]
			if not self.seen[neighbour_index]:
				output += self.dfs(neighbour)			
		return output										# Tips: after invoking dfs(), call clear_labels() to set False all the elements of self.seen
		

	def clear_labels(self):									# set False all the elements of self.seen
		self.seen = [False] * self.__len__()




G = Graph()

G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)
G.add_node(5)
G.add_node(6)

G.add_edge(1,2)
G.add_edge(1,3)
G.add_edge(1,4)
G.add_edge(2,5)
G.add_edge(3,6)
G.add_edge(5,6)

print(len(G))				# print number of vertices of G
print(G[1])				# print the neighbours of the vertex with name 1
print(G.degree(1))

print(G.dfs(1))

print(G.bfs(1))
