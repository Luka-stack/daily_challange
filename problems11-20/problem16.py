"""
You run an e-commerce website and want to record the last N order ids in a log.
Implement a data structure to accomplish this, wtih the follwoing API:
- record(order_id): adds the order_id to the log
- get_last(i): gets the ith last element from the log. I is guaranteed to be smaller 
	than or equal to N
"""


class Logger:

	def __init__(self, max_logs):
		self.buffer = []
		self.max_size = max_logs
		self.next_index = 0


	def record(self, order_id):
		if len(self.buffer) < self.max_size:
			self.buffer.append(order_id)
		else:
			self.buffer[self.next_index] = order_id

		if self.next_index == self.max_size - 1:
			self.next_index = 0
		else:
			self.next_index += 1


	def get_last(self, idx):
		start_index = self.next_index - idx
		if start_index < 0:
			return self.buffer[start_index:] + self.buffer[:self.next_index]
		else:
			return self.buffer[start_index:self.next_index]


def generate_numbers(log, nums):
	for num in range(nums):
		log.record(num)

def main():
	t1 = Logger(5)
	generate_numbers(t1, 6) # Logger[5,1,2,3,4]
	print(t1.get_last(3))
	print(t1.get_last(4))

	t1 = Logger(7)
	generate_numbers(t1, 10) # Logger(7,8,9,3,4,5,6)
	print(t1.get_last(2))

	t1 = Logger(6)
	generate_numbers(t1, 6) # Logger(0,1,2,3,4,5)
	rint(t1.get_last(3))
	t1.record(6) # Logger(0, 1, 2, 3, 4, 5, 6)
	print(t1.get_last(3))
	print(t1.get_last(0))

if __name__ == '__main__':
	main()