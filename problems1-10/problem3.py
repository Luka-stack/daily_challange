"""
Given the root to a binary tree, implement serialize(root), which serializes the tree into a string,
and deserialiaze(s), which deserializes the string back into the tree.

For example, given the following Node class

	class Node:
		def __init__(self, val, left=None, right=None):
			self.val = val
			self.left = left
			self.right = right

The following test should pass:
node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'

I don't know if I understand it corectly so I created two solutions
"""

class Node:

	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right



class BinaryTree:

	def __init__(self, root=None):
		self.root = root

	def add_node(self, node, value):
		if self.root is None:
			self.root = Node(value)
		else:
			if 'left' in value:
				if node.left:
					self.add_node(node.left, value)
				else:
					node.left = Node(value)
			elif 'right' in value:
				if node.right:
					self.add_node(node.right, value)
				else:
					node.right = Node(value)


def serialize(root):
	que = []

	def serializer(node):
		if node:
			que.append(node.val)
			serializer(node.left)
			serializer(node.right)

	serializer(root)

	return ', '.join(que)


def deserialize(s):
	tree = BinaryTree()
	for val in s.split(', '):
		tree.add_node(tree.root, val)

	return tree

def deserialize2(s):
	que = s.split(', ')

	def deserializer2(que):
		if que:
			node = Node(que.pop(0))
			node.left = deserializer2(que)
			node.right = deserializer2(que)

			return node
		return None

	return deserializer2(que)


def main():
	#### Solution 1
	stringes = ['root', 'left', 'left.left', 'right']
	the_tree = BinaryTree()
	for s in stringes:
		the_tree.add_node(the_tree.root, s)

	print(the_tree)
	to_string_1 = serialize(the_tree.root)
	print(to_string_1)
	to_tree = deserialize(to_string_1)
	print(to_tree_1)

	assert deserialize(serialize(the_tree.root)).root.left.left.val == 'left.left'
	####

	#### Solution 2
	node = Node('root', Node('left', Node('left.left')), Node('right'))
	print(node)
	to_string_2 = serialize(node)
	print(to_string_2)
	to_node = deserialize2(to_string_2)
	print(to_node)

	assert deserialize2(serialize(node)).left.left.val == 'left.left'
	####

if __name__ == '__main__':
	main()
