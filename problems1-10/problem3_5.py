"""
Given the root to a Binary Tree, implement serialize(root), which serializes the tree
into a string, and deserialize(s), which deserializes the string back into the tree
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
		if node is None:
			self.root = Node(value)
		else:
			# left
			if value < node.val:
				if node.left is None:
					node.left = Node(value)
				else:
					self.add_node(node.left, value)
			# right
			else:
				if node.right is None:
					node.right = Node(value)
				else:
					self.add_node(node.right, value)


def serialize(root):
	queue = []

	def serializer(node):
		if node:
			queue.append(str(node.val))
			serializer(node.left)
			serializer(node.right)
	serializer(root)

	# return ', '.join(queue)
	return queue

def serialize2(node, queue=None):
	queue = queue if queue else []

	if node:
		queue.append(str(node.val))
		serialize2(node.left, queue)
		serialize2(node.right, queue)

	# return ', '.join(queue)
	return queue


# def deserialize2(s):
# 	queue = iter(s)
# 	tree = BinaryTree()

# 	def deserializer():
# 		val = next(queue)
# 		tree.add_node(tree.root, val)
# 		deserializer()
	
# 	deserializer()
# 	return tree


def deserialize(s):
	tree = BinaryTree()
	# for tk in s.split(', ')
	for tk in s:
			tree.add_node(tree.root, tk)
	#[tree.add_node(tree.root, tk) for tk in s]

	return tree


def main():
	ex_nodes = [4, 2, 9, 1]
	the_tree = BinaryTree()
	for nd in ex_nodes:
		the_tree.add_node(the_tree.root, nd)

	print(f'left:{the_tree.root.left.val} left.left:{the_tree.root.left.left.val}' +
			f' root:{the_tree.root.val} right:{the_tree.root.right.val}')

	ser_res1 = serialize(the_tree.root)
	print(ser_res1)

	des_res1 = deserialize(ser_res1)
	print(f'left:{des_res1.root.left.val} left.left:{des_res1.root.left.left.val}' + 
			f' root:{des_res1.root.val} right:{des_res1.root.right.val}')


if __name__ == '__main__':
	main()