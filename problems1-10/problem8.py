"""
A unival tree (which stands for "universal value") is a tree where
all nodes under it have the same value. Given the root to binary tree,
count the number of unival subtrees.

for example, the following tree has 5 unival subtrees:
	 0
	/ \
   1   0
      / \
     1   0
    / \
   1   1

"""

class Node:

	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right


def count_univals(node):
	total_count, _ = unival_helper(node)
	return total_count


def unival_helper(node):
	if node == None:
		# empty tree is a unival tree but we count only non empty 
		return (0, True)

	# split counter for two subtrees
	left_count, is_left_unival = unival_helper(node.left)
	right_count, is_right_unival = unival_helper(node.right)

	is_unival = True
	# unival tree has consists of unival subtrees
	if not is_left_unival or not is_right_unival:
		is_unival = False

	# unival tree has none children or children with the same value
	if node.left != None and node.left.value != node.value:
		is_unival = False
	if node.right != None  and node.right.value != node.value:
		is_unival = False

	if is_unival:
		return (left_count + right_count + 1, True)
	else:
		return (left_count + right_count, False)


def main():
	binary_tree = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))
	print(count_univals(binary_tree))


if __name__ == '__main__':
	main()
	