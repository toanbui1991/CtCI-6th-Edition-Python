from collections import Counter, heapq
"""
problem: define stack like class which have push, pop
    void push(int val)
    int pop(): remove and return the most frequent element in the stack, if tie choose element which is closet to top

"""

class FreqStack:
	def __init__(self):
		self.heap = []
		self.index = 0
		self.counter = Counter()

	def push(self, val: int) -> None:
		self.counter[val] += 1
		self.index += 1
		heapq.heappush(self.heap, (-self.counter[val], -self.index, val))

	def pop(self) -> int:
		_, _, val = heapq.heappop(self.heap)
		self.counter[val] -= 1
		return val