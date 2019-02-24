"""
Implement locking in a binary tree. A binary tree node can be locked or unlocked only if all
of its descendants of ancestors are not locked.

Design a binary tree node class with the following methods:
	- is_locked, which return whether the node is locked
	- lock, which attempts to lock the node. If it cannot be locked, then it should return False,
		Otherwise, it should lock it and return True
	- unlock, which unlocks the node. If it cannot be unlocked, then it should return False.
		Otherwise, it should unlock it and return true.


Solution -> dailycodingproblem.com/blog/lockable-binary-trees/
"""


class LockingBinaryTreeNode(object):
	
	def __init__(self, val, left=None, right=None, parent=None):
		self.val = val
		self.left = left
		self.right = right
		self.parent = parent
		self.is_locked = False
		self.locked_descendants_nodes = 0


	def is_locked(self):
		return self.is_locked


	def lock(self):
		if self._can_lock_or_unlock():
			self.is_locked = True

			current = self.parent
			while current:
				current.locked_descendants_nodes += 1
				current = current.parent

			return True
		else
			return False


	def unlock(self):
		if self._can_lock_or_unlock():
			self.is_locked = False

			current = self.parent
			while current:
				cur.locked_descendants_nodes -= 1
				current = current.parent

			return True
		else
			return False


	def _can_lock_or_unlock(self):
		if self.locked_descendants_nodes > 0:
			return False

		current = self.parent
		while current:
			if current.is_locked:
				return False
			current = current.parent

		return True

