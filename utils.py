class TreeNode(object):

	def __init__(self, is_leaf=False):
		self.children = {}
		self.is_leaf = is_leaf



class PrefixTree(object):

	def __init__(self):
		self.root = TreeNode()

	def Insert(self, value):
		n = self.root
		for c in value:
			if c not in n.children:
				new_node = TreeNode()
				n.children[c] = new_node
			n = n.children[c]
		n.is_leaf = True


	def _traverse(string, node, results):
		if node.is_leaf:
			results.append(string)
			return

		for c, n in node.children.iteritems():
			_traverse(string + c, n, results)


	def Search(self, value):
		n = self.root
		for c in value:
			if c not in n:
				return False
			else:
				n = n.children

		# value is in tree
		results = []
		traverse(value, n, results)
		return results
