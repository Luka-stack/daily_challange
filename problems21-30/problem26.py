"""
Given a singly linked list and an integer k, remove the kth last element from the list.
K is guaranteed to be smaller than the length of the list.

The list is very long, so making more than one pass is prohibitively expensice.

Do this in constant space and in one pass.
"""


class Node():

	def __init__(self, data=None, next_node=None):
		self.data = data
		self.next_node = next_node


class LinkedList(object):
	
	def __init__(self, head=None):
		self.head = head

	def insert(self, data):
		new_node = Node(data)
		new_node.next_node = self.head
		self.head = new_node


def delete_kth(linked, k):
	curr = linked.head

	for _ in range(k - 1):
		curr = curr.next_node

	#before_k = curr.next_node
	#curr.next_node = before_k.next_node
	#before_k = None
	curr.next_node = curr.next_node.next_node


def main():
	linked_list = LinkedList()
	for d in range(6):
		linked_list.insert(d)

	print("Old List")
	current = linked_list.head
	while current:
		print(current.data)
		current = current.next_node

	delete_kth(linked_list, 4)

	print("New List")
	current = linked_list.head
	while current:
		print(current.data)
		current = current.next_node

if __name__ == '__main__':
	main()
