"""
Given two singly linked lists that intersect at some point, find the intersecting node.
There are non-cyclical

For example. given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node 
with value 8.
"""


class Node(object):

	def __init__(self, data=None, next_node=None):
		self.data = data
		self.next_node = next_node


	def get_data(self):
		return self.data


	def get_next(self):
		return self.next_node


	def set_next(self, new_next):
		self.next_node = new_next


class LinkedList(object):

	def __init__(self, head=None):
		self.head = head


	def insert(self, data):
		new_node = Node(data)
		new_node.set_next(self.head)
		self.head = new_node


	def size(self):
		count, current = 0, self.head
		while current:
			count += 1
			current = current.get_next()
		return count


def get_intesection_node(head_one, head_two):
	count_one = head_one.size()
	count_two = head_two.size()

	if count_one - count_two > 0:
		return get_intesection(count_one - count_two, head_one.head, head_two.head)	
	else:
		return get_intesection(count_two - count_one, head_two.head, head_one.head)

def get_intesection(diff, head_one, head_two):
	current_one, current_two = head_one, head_two
	for _ in range(diff):
		if current_one is None:
			return None
		current_one.get_next()

	while current_one is not None and current_two is not None:
		if current_one.data == current_two.data:
			return current_one.data
		current_one = current_one.next_node
		current_two = current_two.next_node

	return None



def main():
	list_one = LinkedList()
	list_two = LinkedList()

	list_one.insert(10)
	list_one.insert(8)
	list_one.insert(7)
	list_one.insert(3)

	list_two.insert(10)
	list_two.insert(8)
	list_two.insert(1)
	list_two.insert(99)

	print(get_intesection_node(list_one, list_two))


if __name__ == '__main__':
	main()
	