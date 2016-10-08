class TreeNode(object):
	"""Representation of a tree's node."""

	def __init__(self, is_leaf=False):
		self.children = {}
		self.is_leaf = is_leaf


class PrefixTree(object):
    """Implementation of prefix tree."""

    def __init__(self):
        self.root = TreeNode()

    def Insert(self, value):
        """Inserts word into a tree."""
        node = self.root
        for char in value:
            if char not in node.children:
                new_node = TreeNode()
                node.children[char] = new_node
            node = node.children[char]
        node.is_leaf = True

    def _Traverse(self, string, node, results):
        """Traverses tree recursively from given node."""
        if node.is_leaf:
            results.append(string)
            return

        for char, node in node.children.iteritems():
            self._Traverse(string + char, node, results)

    def SearchByPrefix(self, value):
        """Searches for for all words started with given prefix."""
        results = []
        node = self.root
        for char in value:
            if char not in node.children:
                return results
            else:
                node = node.children[char]

        # value is in tree
        self._Traverse(value, node, results)
        return results
