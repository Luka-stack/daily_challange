"""
I implemented thid tree to understand problem nr 3.
"""
class BinaryTree():

	def __init__(self, root_id):
		self.left = None
		self.right = None
		self.root_id = root_id

	def get_left_child(self):
		return self.left

	def get_right_child(self):
		return self.right

	def get_node_value(self):
		return self.root_id

	def set_node_value(self, value):
		self.root_id = value

	def insert_right(self, new_node):
		if self.right == None:
			self.right = BinaryTree(new_node)
		else:
			tree = BinaryTree(new_node)
			tree.right = self.right
			self.right = tree

	def insert_left(self, new_node):
		if self.left == None:
			self.left = BinaryTree(new_node)
		else:
			tree = BinaryTree(new_node)
			tree.left = self.left
			self.left = tree


def print_tree(tree):
	if tree:
		print_tree(tree.get_left_child())
		print(tree.get_node_value())
		print_tree(tree.get_right_child())


def main():
	my_tree = BinaryTree("Taka")
	my_tree.insert_left("Sakai")
	my_tree.insert_right("Sawamura")
	my_tree.insert_right("Maki")
	print_tree(my_tree)


if __name__ == '__main__':
	main()
