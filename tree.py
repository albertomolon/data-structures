
class TreeNode(object):

	def __init__(self, data):
		self.data = data
		self.parent = None
		self.children = []


	def __repr__(self):
		return str(self.data)


	def tree(self):
		output = []

		if self.is_root():
			output.append(str(self.data) + '\n')
		else:
			output.append('  ' * self.depth() + '|-- ' + str(self.data) + '\n')
		if self.children:
			for child in self.children:
				output += child.tree()
		return ''.join(output)
			

	def get_value(self):
		return self.data


	def set_value(self, x):
		self.data = x


	def is_root(self):
		if self.parent == None:
			return True
		else:
			return False


	def is_internal(self):
		if self.children == []:
			return False
		else:
			return True


	def is_external(self):
		if self.children == []:
			return True
		else:
			return False


	def get_parent(self):
		return "Parent: " + self.parent.__repr__()


	def get_children(self):
		try:
			c = [child for child in self.children]
			return c
		except AttributeError:
			return 'Node ' + str(self.data) + ' has not the children attribute.'


	def num_children(self):
		try:
			size = len(self.children)
			return size
		except AttributeError:
			return 'Node ' + str(self.data) + ' has not the children attribute.'


	def size(self):			# return the size of the tree if it is called with root, otherwise the size of a subtree with root 'self'
		size = 1
		for child in self.children:
			size += child.size()
		return size


	def insert(self, child):
		self.child = child
		child.parent = self
		self.children.append(child)


	def height(self):
		h = 0
		for w in self.children:
			h = max(h, 1 + w.height())
		return h


	def depth(self):
		if self.is_root():
			return 0
		else:
			return 1 + self.parent.depth()


	def preorder(self):
		output = []
		output.append(self.data)
		for w in self.children:
			output += w.preorder()
		return output


	def postorder(self):
		output = []
		for w in self.children:
			output += w.postorder()
		output.append(self.data)
		return output




if __name__ == '__main__':
	a = TreeNode('A')
	b = TreeNode('B')
	c = TreeNode('C')
	d = TreeNode('D')
	e = TreeNode('E')
	f = TreeNode('F')
	g = TreeNode('G')

	a.insert(b)
	a.insert(c)
	a.insert(d)
	b.insert(e)
	b.insert(f)
	d.insert(g)

	# print(a)
	print(a.tree())

	# print(a.preorder())
	# print(a.postorder())

