from tree import TreeNode

class BinaryTreeNode(TreeNode):

	def __init__(self, data):
		self.data = data
		self.parent = None
		self.left = None
		self.right = None
		self.children = []


	def insert(self, child):
		if self.left == None:
			self.left = child
			self.children.append(child)
			child.parent = self
		elif self.right == None:
			self.right = child
			self.children.append(child)
			child.parent = self
		else:
			print('You cannot insert', child.data, 'here.')


	def inorder(self):
		output = []
		if self.left != None:
			output += self.left.inorder()
		output.append(self.data)
		if self.right != None:
			output += self.right.inorder()
		return output




if __name__ == '__main__':
	a = BinaryTreeNode('3')
	b = BinaryTreeNode('2')
	c = BinaryTreeNode('7')
	d = BinaryTreeNode('5')
	e = BinaryTreeNode('8')
	f = BinaryTreeNode('4')
	g = BinaryTreeNode('6')

	a.insert(b)
	a.insert(c)
	c.insert(d)
	c.insert(e)
	d.insert(f)
	d.insert(g)

	print(a.tree())

